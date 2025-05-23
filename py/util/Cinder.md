### Cinder
- Cinder在OpenStack中为虚拟机实例提供volume的块存储服务，可将卷挂载到实例上，作为虚拟机实例的本地磁盘使用。
    - **组件化**：便于添加新功能
    - **高可用**：能承受高负载
    - **容错**：隔离机制避免级联故障
    - **可恢复**：简便及时的故障检测与恢复
    - **开放标准**：提供标准实现，为社区提供参考

#### 主要模块
![image](http://www.99cloud.net/wp-content/uploads/2019/04/7-1554090785.jpg)
##### cinder-api
- 对外提供稳定而统一的北向 RESTful API，cinder-api service 服务进程通常运行在控制节点，支持多 Workers 进程（通过配置项 osapivolumeworkers 设定）。接收到的合法请求会经由 MQ 传递到 cinder-volume 执行。Cinder API 现存 v2(DEPRECATED)、v3(CURRENT) 两个版本，可以通过配置文件来启用。
- 官方API介绍：https://developer.openstack.org/api-ref/block-storage/

###### 核心流程
- 创建 Volume  的流程：
    - cinder-api 创建 volume_create_api 工作流（flow） 
        - ExtractVolumeRequestTask：获取（Extract）、验证（Validates）create volume 在 cinder-api 阶段相关的信息
        - QuotaReserverTask：预留配额
        - EntryCreateTask：在数据库中创建 Volumn 条目
        - QuotaCommitTask：确认配额 
        - VolumeCastTask：发出一个 Cast 异步请求，将创建请求丢到 MQ，最终被 cinder-scheduler service 接收
    - cinder-scheduler 启动一个 volume_create_scheduler flow
        - ExtractSchedulerSpecTask：将 request body 转换成为 Scheduler Filter 中通用的 RequestSpec 数据结构（实例对象）。
        - SchedulerCreateVolumeTask：完成 Filter 和 Weight 的调度算法。
    - RPC 请求发送到 cinder-volume service 接收
    - cinder-volume 启动工作流 volume_create_manager：
        - ExtractVolumeRefTask ： 解析请求体
        - OnFailureRescheduleTask：
        - ExtractVolumeSpecTask：将 request body 转换成为 Volume 模块中通用的 RequestSpec 数据结构（实例对象）
        - NotifyVolumeActionTask：当对已有的卷采取措施的时候发送相应的通知 
        - CreateVolumeFromSpecTask：创建对应的卷 
        - CreateVolumeFromSpecTask：执行创建成功之后的后续操作 
- 创建 Volume 的方式
   - 建立raw格式的新卷
   - 从快照建立新卷
   - 从已有卷建立新卷
   - 从副本建立新卷
   - 从镜像建立新卷

###### 细节 
根据现在最新的[ V3 ](https://developer.openstack.org/api-ref/block-storage/v3/index.html)版本的 API总结如下:
- [Github: Volume 资源模型](https://github.com/openstack/cinder/blob/master/cinder/db/sqlalchemy/models.py)
- Volumn Type 主要是针对多后端存储进行卷类型的管理  
![image](https://img-blog.csdnimg.cn/20190225183417599.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ptaWxr,size_16,color_FFFFFF,t_70)  
- Volumes 针对 卷 来进行管理。其中一个卷（Volume）类似于一个如USB硬盘的可插拔的块存储设备，每一次可以将卷对应的挂载到实例上。
    - 对 Volumes 设备进行 CRUD 时，对应的会有很多种状态，可以参考对应官方文档中的状态表。
    - CRUD of Cinder Volumn

###### CRUD of Cinder Volumn
- POST  `/v3/{project_id}/volumes` Request Body  
```JSON
{
    "volume": {
        "size": 10,      //int The size of the volume, in gibibytes (GiB).
        "availability_zone": null, //The name of the availability zone.
        "source_volid": null, //The UUID of the source volume.
        "description": null, //The volume description.
        "multiattach": false, //To enable this volume to attach to more than one server, set this value to true. Default is false.
        "snapshot_id": null, //The UUID of the volume snapshot
        "backup_id": null, //The UUID of the backup.
        "name": null, //The volume name.
        "imageRef": null, //The UUID of the image from which you want to create the volume. 
        <!--"volume_type": null, //The volume type (either name or ID). 
        "metadata": {}, //One or more metadata key and value pairs to be associated with the new volume.
        "consistencygroup_id": null //The UUID of the consistency group.
    },
    "OS-SCH-HNT:scheduler_hints": { //The dictionary of data to send to the scheduler.
        "same_host": [
            "a0cf03a5-d921-4877-bb5c-86d26cf818e1",
            "8c19174f-4220-44f0-824a-cd1eeef10287"
        ]
    }
}
```
- POST `/v3/{project_id}/volumes` Response Body
``` JSON
{
    "volume": {
        "attachments": [], //Instance attachment information.(Server/Host/Device/Volume)
        "availability_zone": "nova",//The name of the availability zone.
        "bootable": "false",//Enables or disables the bootable attribute. You can boot an instance from a bootable volume.
        "consistencygroup_id": null,//The UUID of the consistency group.
        "created_at": "2018-11-28T06:21:12.715987",//The date and time when the resource was created.CCYY-MM-DDThh:mm:ss±hh:mm
        "description": null, //The volume description.
        "encrypted": false, //If true, this volume is encrypted.
        "id": "2b955850-f177-45f7-9f49-ecb2c256d161",//The UUID of the volume.
        "links": [ //The volume links.
            {
                "href": "http://127.0.0.1:33951/v3/89afd400-b646-4bbc-b12b-c0a4d63e5bd3/volumes/2b955850-f177-45f7-9f49-ecb2c256d161",
                "rel": "self"
            },
            {
                "href": "http://127.0.0.1:33951/89afd400-b646-4bbc-b12b-c0a4d63e5bd3/volumes/2b955850-f177-45f7-9f49-ecb2c256d161",
                "rel": "bookmark"
            }
        ],
        "metadata": {},//A metadata object. Contains one or more metadata key and value pairs that are associated with the volume.
        "migration_status": null,
        "multiattach": false,//If true, this volume can attach to more than one instance.
        "name": null,//The volume name.
        "replication_status": null,//The volume replication status.
        "size": 10,//The size of the volume, in gibibytes (GiB).
        "snapshot_id": null,// The UUID of the volume snapshot
        "source_volid": null,//The UUID of the source volume.
        "status": "creating",//The volume status.
        "updated_at": null, //The date and time when the resource was updated. CCYY-MM-DDThh:mm:ss±hh:mm
        "user_id": "c853ca26-e8ea-4797-8a52-ee124a013d0e",//The UUID of the user.
        "volume_type": null //The associated volume type for the volume.
    }
```

- GET `/v3/{project_id}/volumes` (List accessible volumes) Response Body
```JSON
{
    "volumes": [
        {
            "id": "efa54464-8fab-47cd-a05a-be3e6b396188",
            "links": [
                {
                    "href": "http://127.0.0.1:37097/v3/89afd400-b646-4bbc-b12b-c0a4d63e5bd3/volumes/efa54464-8fab-47cd-a05a-be3e6b396188",
                    "rel": "self"
                },
                {
                    "href": "http://127.0.0.1:37097/89afd400-b646-4bbc-b12b-c0a4d63e5bd3/volumes/efa54464-8fab-47cd-a05a-be3e6b396188",
                    "rel": "bookmark"
                }
            ],
            "name": null
        }
    ]
}
```

- GET `/v3/{project_id}/volumes/{volume_id}` Response Body
```JSON
{
    "volume": {
        "attachments": [],
        "availability_zone": "nova",
        "bootable": "false",
        "consistencygroup_id": null,
        "created_at": "2018-11-29T06:50:07.770785",
        "description": null,
        "encrypted": false,
        "id": "f7223234-1afc-4d19-bfa3-d19deb6235ef",
        "links": [
            {
                "href": "http://127.0.0.1:45839/v3/89afd400-b646-4bbc-b12b-c0a4d63e5bd3/volumes/f7223234-1afc-4d19-bfa3-d19deb6235ef",
                "rel": "self"
            },
            {
                "href": "http://127.0.0.1:45839/89afd400-b646-4bbc-b12b-c0a4d63e5bd3/volumes/f7223234-1afc-4d19-bfa3-d19deb6235ef",
                "rel": "bookmark"
            }
        ],
        "metadata": {},
        "migration_status": null,
        "multiattach": false,
        "name": null,
        "os-vol-host-attr:host": null,//Current back-end of the volume. Host format is host@backend#pool.
        "os-vol-mig-status-attr:migstat": null,//The status of this volume migration (None means that a migration is not currently in progress).
        "os-vol-mig-status-attr:name_id": null,//The volume ID that this volume name on the back- end is based on.
        "os-vol-tenant-attr:tenant_id": "89afd400-b646-4bbc-b12b-c0a4d63e5bd3",//The project ID which the volume belongs to.
        "replication_status": null,
        "size": 10,
        "snapshot_id": null,
        "source_volid": null,
        "status": "creating",
        "updated_at": null,
        "user_id": "c853ca26-e8ea-4797-8a52-ee124a013d0e",
        "volume_type": null
    }
}
```

- PUT `/v3/{project_id}/volumes/{volume_id}` Request Body
```JSON
{
    "volume": {
        "name": "vol-003",
        "description": "This is yet, another volume.",
        "metadata": {
            "name": "metadata0"
        }
    }
}
```

- DELETE `/v3/{project_id}/volumes/{volume_id}`
    - Preconditions: status available, in-use, error, error_restoring, error_extending, error_managing.
    - Async Postconditions: Delete index and volumn on storage node.

###### CRUD of Cinder Volumn metadata
- POST `/v3/{project_id}/volumes/{volume_id}/metadata` Request Body (Same with response)
```JSON
{
    "metadata": {
        "name": "metadata0"
    }
}
```

- GET `/v3/{project_id}/volumes/{volume_id}/metadata`
- PUT `/v3/{project_id}/volumes/{volume_id}/metadata` 
- GET `/v3/{project_id}/volumes/{volume_id}/metadata/{key}` //Show a volume’s metadata for a specific key
- DELETE `/v3/{project_id}/volumes/{volume_id}/metadata/{key}`
- PUT `/v3/{project_id}/volumes/{volume_id}/metadata/{key}`
- GET `/v3/{project_id}/volumes/summary` Response Body //Get volumes summary 
```JSON
{
    "volume-summary": {
        "total_size": 4,
        "total_count": 4,
        "metadata": {
            "key1": ["value1", "value2"],
            "key2": ["value2"]
        }
    }
}
```

###### Volume manage extension (manageable_volumes)¶
- POST `/v3/{project_id}/manageable_volumes` 
- Creates a Block Storage volume by using existing storage rather than allocating new storage.
```JSON
Request
{
    "volume": {
        "host": "geraint-VirtualBox",
        "ref": {
            "source-name": "existingLV",
            "source-id": "1234"
        },
        "name": "New Volume",
        "availability_zone": "az2",
        "description": "Volume imported from existingLV",
        "volume_type": null,
        "bootable": true,
        "metadata": {
            "key1": "value1",
            "key2": "value2"
        }
    }
}
```

- GET `/v3/{project_id}/manageable_volumes` List summary of volumes available to manage
```JSON
Response
{
    "manageable-volumes": [
        {
            "safe_to_manage": false,
            "reference": {
                "source-name": "volume-3a81fdac-e8ae-4e61-b6a2-2e14ff316f19"
            },
            "size": 1
        },
        {
            "safe_to_manage": true,
            "reference": {
                "source-name": "lvol0"
            },
            "size": 1
        }
    ]
}
```

- GET `/v3/{project_id}/manageable_volumes/detail` List detail of volumes available to manage
```JSON
Response
{
    "manageable-volumes": [
        {
            "cinder_id": "9ba5bb53-4a18-4b38-be06-992999da338d",
            "reason_not_safe": "already managed",
            "reference": {
                "source-name": "volume-9ba5bb53-4a18-4b38-be06-992999da338d"
            },
            "safe_to_manage": false,
            "size": 1,
            "extra_info": null
        },
        {
            "cinder_id": null,
            "reason_not_safe": null,
            "reference": {
                "source-name": "lvol0"
            },
            "safe_to_manage": true,
            "size": 1,
            "extra_info": null
        }
    ]
}
```
###### Volume transfer 
- Transfers a volume from one user to another user.

###### Services (os-services)¶
- Administrator only. Lists all Cinder services, enables or disables a Cinder service, freeze or thaw the specified cinder-volume host, failover a replicating cinder-volume host.


###### Volume actions (volumes, action)¶
- POST `/v3/{project_id}/volumes/{volume_id}/action`
```JSON
{
    // Extend the size
    "os-extend": {
        "new_size": 3
    }
    
    // Reset a volume’s statuses
    "os-reset_status": {
        "status": "available",
        "attach_status": "detached",
        "migration_status": "migrating"
    }
    
    // Revert volume to snapshot
    "revert": {
        "snapshot_id": "5aa119a8-d25b-45a7-8d1b-88e127885635"
    }
    
    // Set image metadata for a volume
    "os-set_image_metadata": {
        "metadata": {
            "image_id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c",
            "image_name": "image",
            "kernel_id": "155d900f-4e14-4e4c-a73d-069cbf4541e6",
            "ramdisk_id": "somedisk"
        }
    }
    
    // Remove image metadata from a volume
    "os-unset_image_metadata": {
        "key": "ramdisk_id"
    }
    
    // Show image metadata for a volume
    "os-show_image_metadata": {}

    // Attach volume to a server
    "os-attach": {
        "instance_uuid": "95D9EF50-507D-11E5-B970-0800200C9A66", //The UUID of the attaching instance.
        "mountpoint": "/dev/vdc" //The attaching mount point.
    }
    
    // Detach volume from server
    "os-detach": {
        "attachment_id": "d8777f54-84cf-4809-a679-468ffed56cf1"
    }
    
    // Unmanage a volume
    "os-unmanage": {}
    
    // Force detach a volume
    "os-force_detach": {
        "attachment_id": "d8777f54-84cf-4809-a679-468ffed56cf1",
        "connector": {
            "initiator": "iqn.2012-07.org.fake:01"
        }
    }
    
    //Retype a volume
    //Migrate a volume
    //Complete migration of a volume
    //Force delete a volume
    //Update a volume’s bootable status
    //Upload volume to image
    //Reserve volume
    //Unmark volume as reserved.
    //Update volume status to detaching
    //Roll back volume status to in-use
    //Terminate volume attachment
    //Initialize volume attachment
    //Updates volume read-only access-mode flag
    ...
}
```

###### Generic volume groups
- Generic volume groups enable you to create a group of volumes and manage them together.





##### cinder-scheduler
- 如果说 cinder-api 接收的是关于 “创建” 的请求（e.g. Create Volume），那么该请求就会通过 MQ 转发到 cinder-scheduler service 服务进程，cinder-scheduler 与 nova-scheduler 一般，顾名思义是调度的层面。通过 Filters 选择最 “合适” 的 Storage Provider Node 来对请求资源（e.g. Volume）进行创建。不同的 Filters 具有不同的过滤（调度）算法，所谓的 “合适” 就是达到客户预期的结果，用户还可以自定义 Filter Class 来实现符合自身需求的过滤器，让调度更加灵活。与 nova-scheduler 一般，cinder-scheduler 同样需要维护调度对象（存储节点）“实时” 状态，cinder-volume service 会定期的向 cinder-scheduler service 上报存储节点状态（注：这实际上是通过后端存储设备的驱动程序上报了该设备的状态）。

    - 首先判断存储节点状态，只有状态为 up 的存储节点才会被考虑。
    - 创建 Volume 时，根据 Filter 和 Weight 算法选出最优存储节点。
    - 迁移 Volume 时，根据 Filter 和 Weight 算法来判断目的存储节点是否符合要求。

##### cinder-volume
- cinder-volume service 是 Cinder 的核心服务进程，运行该服务进程的节点都可以被称之为存储节点。cinder-volume 通过抽象出统一的 Back-end Storage Driver 层，让不同存储厂商得以通过提供各自的驱动程序来对接自己的后端存储设备，实现即插即用（通过配置文件指定），多个这样的存储节点共同构成了一个庞大而复杂多样的存储资源池系统。

###### cinder-volumn Driver
- OpenStack 作为开放的 Infrastracture as a Service 云操作系统，支持业界各种优秀的技术，这些技术可能是开源免费的，也可能是商业收费的。 这种开放的架构使得 OpenStack 保持技术上的先进性，具有很强的竞争力，同时又不会造成厂商锁定（Lock-in）。
- 以 Cinder 为例，存储节点支持多种 Volume Provider，包括 LVM、NFS、Ceph、GlusterFS 以及 EMC、IBM 等商业存储系统。 cinder-volume 为这些 Volume Provider 抽象了统一的 Driver 接口，Volume Provider 只需要实现这些接口，就可以以 Driver 的形式即插即（volume_driver 配置项）用到 OpenStack 中。下面是 Cinder Driver 的架构示意图：  
![image](http://www.99cloud.net/wp-content/uploads/2019/04/4-1554090785.jpg)

##### cinder-volumn Plugin
- Driver 和 Plugin 通常不会分家，Driver 是由各存储厂商提供的，那么 Plugins（插槽）就应该有 Cinder 的提供。 根据 FileSystem Storage 和 Block Storage 两个不同类型的外部存储系统，Cinder Plugins 也提供了 FileSystem based 和 Block based 两种不同类型 Plugin。除此之外，Cinder Plugins 还提供了 iSCSC、FC、NFS 等常用的数据传输协议 Plugin 框架，上传逻辑得以根据实际情况来使用（Attached/Dettached）存储资源。

##### cinder-backup
- 提供 Volume 的备份功能，支持将 Volume 备份到对象存储中（e.g. Swift、Ceph、IBM TSM、NFS），也支持从备份 Restore 成为 Volume。


#### 参考链接
- [[1] OpenStack: Cinder官方文档](https://docs.openstack.org/cinder/latest/)
- [[2] 博客园：Cinder 组件解析](https://www.cnblogs.com/luohaixian/p/8134967.html)
- [[3] ZhiHu: OpenStack-Cinder ](https://zhuanlan.zhihu.com/p/34634620)
- [[4] Github Repo: OpenStack/Cinder](https://github.com/openstack/cinder)
- [[5] 九州云：CINDER 架构分析、高可用部署与核心功能解析](http://www.99cloud.net/10758.html%EF%BC%8F)
- [[6] 博客园：Cinder 架构分析、高可用部署与核心功能解析](https://www.cnblogs.com/jmilkfan-fanguiju/p/10589720.html)