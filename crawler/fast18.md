### Failing and Recovering 

#### 1. Fail-Slow at Scale: Evidence of Hardware Performance Faults in Large Production Systems. 
- [Source](https://www.usenix.org/conference/fast18/presentation/gunawi) 

##### Abstract 
- Fail-slow hardware is an under-studied failure mode. We present a study of 101 reports of fail-slow hardware incidents, collected from large-scale cluster deployments in 12 institutions. We show that all hardware types such as disk, SSD, CPU, memory and network components can exhibit performance faults. We made several important observations such as faults convert from one form to another, the cascading root causes and impacts can be long, and fail-slow faults can have varying symptoms. From this study, we make suggestions to vendors, operators, and systems designers. 

#### 2. Protocol-Aware Recovery for Consensus-Based Storage. 
- [Source](https://www.usenix.org/conference/fast18/presentation/alagappan) 

##### Abstract 
- We introduce protocol-aware recovery (PAR), a new approach that exploits protocol-specific knowledge to correctly recover from storage faults in distributed systems. We demonstrate the efficacy of PAR through the design and implementation of corruption-tolerant replication (CTRL), a PAR mechanism specific to replicated state machine (RSM) systems. We experimentally show that the CTRL versions of two systems, LogCabin and ZooKeeper, safely recover from storage faults and provide high availability, while the unmodified versions can lose data or become unavailable. We also show that the CTRL versions have little performance overhead. 

#### 3. WAFL Iron: Repairing Live Enterprise File Systems. 
- [Source](https://www.usenix.org/conference/fast18/presentation/kesavan) 

##### Abstract 
- Consistent and timely access to an arbitrarily damaged file system is an important requirement of enterprise class systems. Repairing file system inconsistencies is accomplished most simply when file system access is limited to the repair tool. Checking and repairing a file system while it is open for general access present unique challenges. In this paper, we explore these challenges, present our online repair tool for the NetApp® WAFL® file system, and show how it achieves the same results as offline repair even while client access is enabled. We present some implementation details and evaluate its performance. To the best of our knowledge, this publication is the first to describe a fully functional online repair tool. 

### Revealing Flashy Secrets 

#### 1. MQSim: A Framework for Enabling Realistic Studies of Modern Multi-Queue SSD Devices. 
- [Source](https://www.usenix.org/conference/fast18/presentation/tavakkol) 

##### Abstract 
- Solid-state drives (SSDs) are used in a wide array of computer systems today, including in datacenters and enterprise servers.  As the I/O demands of these systems have increased, manufacturers have evolved SSD design to keep up with this demand.  For example, manufacturers have introduced new high-bandwidth interfaces to replace the traditional SATA protocol.  These new interfaces, such as the NVMe protocol, are designed specifically to enable the high amount  of concurrent I/O that SSDs are capable of delivering. 

- While modern SSDs with sophisticated features such as the NVMe protocol are  already on the market, SSD simulation tools have fallen behind, as they do not capture these new features.  We compare the outputs of these simulators  to the performance measured from real off-the-shelf SSDs, and find three major shortcomings in state-of-the-art SSD simulators. 

- First, existing simulators do not model critical features of new protocols like  NVMe, such as their use of multiple application-level queues for requests and the elimination of OS intervention. Second, existing simulators do not capture the effects of advanced SSD maintenance algorithms (e.g., garbage collection), as they do not properly emulate the steady-state conditions that exist in real SSDs. Third, existing simulators do not capture the full end-to-end latency of I/O requests, which can incorrectly skew the simulated behavior of SSDs that use emerging memory technologies, such as 3D XPoint. We show that without the accurate modeling of these features, results from existing simulators deviate significantly from real SSD performance. 

- In this work, we introduce a new simulator, called MQSim, that accurately models the performance of both modern SSDs and conventional SATA-based SSDs. MQSim faithfully models new high-bandwidth protocol implementations, steady-state SSD conditions, and the full end-to-end latency for requests in modern SSDs.   We validate MQSim using several modern SSDs, and show that MQSim uncovers several real and important issues that were not captured by existing simulators, such as the performance impact of inter-flow interference in modern SSDs. We plan to release MQSim as an open-source tool, and we hope that it can enable several new research directions in the future. 

#### 2. PEN: Design and Evaluation of Partial-Erase for 3D NAND-Based High Density SSDs. 
- [Source](https://www.usenix.org/conference/fast18/presentation/liu) 

##### Abstract 
- 3D NAND flash memories promise unprecedented flash storage capacities, which can be extremely important in certain application domains where both storage capacity and performance are first-class target metrics. However a block of 3D NAND flash contains many more pages than its 2D counterpart. This increased number of pages-per-block has numerous ramifications such as the longer erase latency, higher garbage collection costs, and increased write amplification factors, which can collectively prevent the 3D NAND flash products from becoming the mainstream in high-performance storage domain. In this paper, we introduce PEN, an architecture-level mechanism that enables partial-erase of flash blocks. Using our proposed partial-erase support, we also discuss how one can build a custom garbage collector for two types of flash translation layers (FTLs), namely, block-level FTL and hybrid FTL. Our experimental evaluations of PEN with a set of diverse real storage workloads indicate that the proposed approach can shorten the write latency by $44.3\%$ and $47.9\%$ for block-level FTL and hybrid FTL, respectively. 

#### 3. The CASE of FEMU: Cheap, Accurate, Scalable and Extensible Flash Emulator. 
- [Source](https://www.usenix.org/conference/fast18/presentation/li) 

##### Abstract 
- We present FEMU, a QEMU-based flash emulator for fostering future full-stack software/hardware SSD research, with the following four "CASE" benefits. FEMU is cheap ($0) as it will be an open-sourced software; FEMU is relatively accurate, with only 0.5-38% variance from OpenChannel SSD in our tests; FEMU is scalable, upon our optimized QEMU stack, to support up to 32 parallel channels/chips without unintended queueing 

- delays; FEMU is extensible, enabling various types of SSD research, such as internal-SSD, kernel-only and split-level research on it. 

### Understanding the Meta(data) Story 

#### 1. Spiffy: Enabling File-System Aware Storage Applications. 
- [Source](https://www.usenix.org/conference/fast18/presentation/sun) 

##### Abstract 
- Many file system applications such as defragmentation tools, file system checkers or data recovery tools, operate at the storage layer. Today, developers of these storage applications require detailed knowledge of the file system format, which takes a significant amount of time to learn, often by trial and error, due to insufficient documentation or specification of the format. Furthermore, these applications perform ad-hoc processing of the file-system metadata, leading to bugs and vulnerabilities.  

- We propose Spiffy, an annotation language for specifying the on-disk format of a file system. File system developers annotate the data structures of a file system, and we use these annotations to generate a library that allows identifying, parsing and traversing file-system metadata, providing support for both offline and online storage applications. This approach simplifies the development of storage applications that work across different file systems because it reduces the amount of file-system specific code that needs to be written. 

- We have written annotations for the Linux Ext4, Btrfs and F2FS file systems, and developed several applications for these file systems, including a type-specific metadata corruptor, a file system converter, and an online storage layer cache that preferentially caches files for certain users. Our experiments show that applications that use the library to access file system metadata can achieve good performance and are robust against file system corruption errors. 

#### 2. Towards Robust File System Checkers. 
- [Source](https://www.usenix.org/conference/fast18/presentation/gatla) 

##### Abstract 
- File systems may become corrupted for many reasons despite various protection techniques. Therefore, most file systems come with a checker to recover the file system to a consistent state. However, existing checkers are commonly assumed to be able to complete the repair without interruption, which may not be true in practice. 

- In this work, we demonstrate via fault injection experiments that checkers of widely used file systems may leave the file system in an uncorrectable state if the repair procedure is interrupted unexpectedly. To address the problem, we first fix the ordering issue in the undo logging of e2fsck, and then build a general logging library (i.e., rfsck-lib) for strengthening checkers. To demonstrate the practicality, we integrate rfsck-lib with existing checkers and create two new checkers: (1) rfsck-ext, a robust checker for Ext-family file systems, and (2) rfsck-xfs, a robust checker for XFS file system, both of which require only tens of lines of modification to the original versions. Both rfsck-ext and rfsck-xfs are resilient to faults in our experiments. Also, both checkers incur reasonable performance overhead (i.e., up to 12%) comparing to the original unreliable versions. Moreover, rfsck-ext outperforms the patched e2fsck by up to nine times while achieving the same level of robustness. 

#### 3. The Full Path to Full-Path Indexing. 
- [Source](https://www.usenix.org/conference/fast18/presentation/zhan) 

##### Abstract 
- This paper shows how to use full-path indexing in a file system to realize fast directory scans, writes, and renames. Prior results indicated that renames are prohibitively expensive in full-path indexing. 

- The paper introduces a range-rename mechanism for efficient key-space changes in a write-optimized dictionary. This mechanism is encapsulated in the key-value-store API, and simplifies the overall design of the file system. 

- We implemented this mechanism in ArborFS, an extension of the BetrFS in-kernel, local file system for Linux. For instance, ArborFS performs recursive greps 1.5x faster and random writes 1.2x faster than BetrFS, but renames are competitive with standard, indirection-based file systems for a range of sizes. ArborFS outperforms relative-path file systems such as BetrFS as well as traditional file systems such as ext4, xfs and zfs across a variety of workloads. 

### Coding, Hashing, Hiding 

#### 1. Clay Codes: Moulding MDS Codes to Yield an MSR Code. 
- [Source](https://www.usenix.org/conference/fast18/presentation/vajha) 

##### Abstract 
- With increase in scale, the number of node failures in a data center increases sharply.  To ensure availability of data, failure-tolerance schemes such as Reed-Solomon (RS) or more generally, Maximum Distance Separable (MDS) erasure codes are used. However, while MDS codes offer minimum storage overhead for a given amount of failure tolerance, they do not meet other practical needs of today's data centers. Although modern codes such as Minimum Storage Regenerating (MSR) codes are designed to meet these practical needs, they are available only in highly-constrained theoretical constructions, that are not sufficiently mature enough for practical implementation.  We present {\em Clay codes} that extract the best from both worlds. Clay (short for Coupled-Layer) codes are MSR codes that offer a simplified construction for decoding/repair by using pairwise coupling across multiple stacked layers of any single MDS code. 

- In addition, Clay codes provide the first practical implementation of an MSR code that offers (a) low storage overhead, (b) simultaneous optimality in terms of three key parameters: repair bandwidth, sub-packetization level and disk I/O, (c) uniform repair performance of data and parity nodes and (d) support for both single and multiple-node repairs, while permitting faster and more efficient repair. 

- While all MSR codes are vector codes, none of the distributed storage systems support vector codes. We have modified Ceph to support any vector code, and our contribution is now a part of Ceph's master codebase. We have implemented Clay codes, and integrated it as a plugin to Ceph. Six example Clay codes were evaluated on a cluster of Amazon EC2 instances and code parameters were carefully chosen to match known erasure-code deployments in practice. A particular example code, with storage overhead $1.25$x, is shown to reduce repair network traffic by a factor of $2.9$ in comparison with RS codes and similar reductions are obtained for both repair time and disk read. 

#### 2. Towards Web-based Delta Synchronization for Cloud Storage Services. 
- [Source](https://www.usenix.org/conference/fast18/presentation/xiao) 

##### Abstract 
- Delta synchronization (sync) is crucial for network-level efficiency of cloud storage services. Practical delta sync techniques are, however, only available for PC clients and mobile apps, but not web browsers---the most pervasive and OS-independent access method.  To understand the obstacles of web-based delta sync, we implement a delta sync solution, WebRsync, using state-of-the-art web techniques based on rsync, the de facto delta sync protocol for PC clients. Our measurements show that WebRsync severely suffers from the inefficiency of JavaScript execution inside web browsers, thus leading to frequent stagnation and even hanging. 

- Given that the computation burden on the web browser mainly stems from data chunk search and comparison, we reverse the traditional delta sync approach by lifting all chunk search and comparison operations from the client side to the server side. Inevitably, this brings considerable computation overhead to the servers. Hence, we further leverage locality-aware chunk matching and lightweight checksum algorithms to reduce the overhead. The resulting solution, WebR2sync+, outpaces WebRsync by an order of magnitude, and is able to simultaneously support 6800--8500 web clients' delta sync using a standard VM server instance based on a Dropbox-like system architecture. 

#### 3. Stash in a Flash. 
- [Source](https://www.usenix.org/conference/fast18/presentation/zuck) 

##### Abstract 
- Encryption is a useful tool to protect data confidentiality. Yet it is still challenging to hide the very presence of encrypted, secret data from a powerful adversary. This paper presents a new technique to hide data in flash by manipulating the voltage level of pseudo-randomlyselected flash cells to encode two bits (rather than one) in the cell. In this model, we have one “public” bit interpreted using an SLC-style encoding, and extract a private bit using an MLC-style encoding. The locations of cells that encode hidden data is based on a secret key known only to the hiding user. 

- Intuitively, this technique requires that the voltage level in a cell encoding data must be (1) not statistically distinguishable from a cell only storing public data, and (2) the user must be able to reliably read the hidden data from this cell. Our key insight is that there is a wide enough variation in the range of voltage levels in a typical flash device to obscure the presence of fine-grained changes to a small fraction of the cells, and that the variation is wide enough to support reliably re-reading hidden data. We demonstrate that our hidden data and underlying voltage manipulations go undetected by support 

- vector machine based supervised learning which performs similarly to a random guess. The error rates of our scheme are low enough that the data is recoverable months after being stored. Compared to prior work, our technique provides 24x and 50x higher encoding and decoding throughput and doubles the capacity, while being 37x more power efficient. 

### New Media and Old 

#### 1. Endurable Transient Inconsistency in Byte-Addressable Persistent B+-Tree. 
- [Source](https://www.usenix.org/conference/fast18/presentation/hwang) 

##### Abstract 
- With the emergence of byte-addressable persistent memory (PM), a cache line, instead of a page, is expected to be the unit of data transfer between volatile and nonvolatile devices, but the failure-atomicity of write operations is guaranteed in the granularity of 8 bytes rather than cache lines. This granularity mismatch problem has generated interest in redesigning block-based data structures such as B+-trees, and attempts have been made to use in-memory data structures for PM. However, various methods of modifying B+-trees for PM degrade the efficiency of B+-trees due to the additional metadata and high rebalancing overhead caused by logging methods. 

- In this study, we develop Failure-Atomic ShifT (FAST) and Failure-Atomic In-place Rebalance (FAIR) algorithms.  FAST and FAIR modify legacy B+-trees in a byte-addressable fashion but solves the granularity mismatch problem.  Every 8-byte store instruction used in the FAST and FAIR algorithms transforms a B+-tree into another consistent state or a transient inconsistent state that read operations can tolerate.  By making read operations transient inconsistency, we can eliminate expensive copy-on-write, logging, and even the necessity of read latches so that read transactions can be non-blocking.   Our experimental results show that legacy B+-trees with FAST and FAIR schemes outperform the state-of-the-art persistent indexing structures by a large margin. 

#### 2. RFLUSH: Rethink the Flush. 
- [Source](https://www.usenix.org/conference/fast18/presentation/yeon) 

##### Abstract 
- A FLUSH command has been used for decades to enforce persistence and ordering of updates in a storage device. The command forces all the data in the volatile buffer to non-volatile media to achieve persistency. This lumpsum approach to flushing has two performance consequences. First, it slows down non-volatile materialization of the writes that actually need to be flushed. Second, it deprives the writes that need not to be flushed of an opportunity for absorbing future writes and coalescing. We attempt to characterize the problems of this semantic gap of flushing in storage devices and propose RFLUSH that allows a fine-grained control over flushing in them. The RFLUSH command delivers a range of LBAs that need to be flushed and thus enables the storage device to force only a subset of data in its buffer. We implemented this fine-grained flush command in a storage device using an open-source flash development platform and modified the F2FS file system to make use of the command in processing fsync requests as a case study. Performance evaluation using the prototype implementation shows that the inclusion of RFLUSH improves the throughput by up to 5.6x; reduces the write traffic by up to 43%; and eliminates the long tail in the response time. 

#### 3. Barrier-Enabled IO Stack for Flash Storage. 
- [Source](https://www.usenix.org/conference/fast18/presentation/won) 

##### Abstract 
- This work is dedicated to eliminating the overhead required for guaranteeing the storage order in the modern IO stack. The existing block device adopts a prohibitively expensive approach in ensuring the storage  order among write requests: interleaving the write requests  with Transfer-and-Flush. Exploiting the cache barrier command for Flash storage, we overhaul the IO scheduler, the dispatch module, and the filesystem so that these layers are orchestrated to preserve the ordering condition imposed by the application with which the associated data blocks are made durable. The key ingredients of Barrier-Enabled IO stack are Epoch-based IO scheduling, Order-Preserving Dispatch, and Dual-Mode Journaling. Barrier-enabled IO stack can control the storage order without Transfer-and-Flush overhead. We implement the barrier-enabled IO stack in server as well as in mobile platforms. SQLite performance increases by 270% and  75%, in server and in smartphone, respectively. In a server storage, BarrierFS brings as much as by 43$\times$ and by 73$\times$ performance gain in MySQL and SQLite, respectively, against EXT4 via relaxing the durability of a transaction. 

### Long Live the File System! 

#### 1. High-Performance Transaction Processing in Journaling File Systems. 
- [Source](https://www.usenix.org/conference/fast18/presentation/son) 

##### Abstract 
- Journaling file systems provide crash-consistency to applications by keeping track of uncommitted changes in the journal area (journaling) and writing committed changes to their original area at a certain point (checkpointing). They generally use coarse-grained locking to access shared data structures and perform I/O operations by a single thread. For these reasons, journaling file systems often face the problem of lock contention and underutilization of I/O bandwidth on multi-cores with high-performance storage.  To address these issues, we design journaling and checkpointing schemes that enable concurrent updates on data structures and parallelize I/O operations.  We implement our schemes in EXT4/JBD2 and evaluate them on a 72-core machine with a high-performance NVMe SSD. The experimental results show that our optimized file system improves the performance by up to about 2.2x and 1.5x compared to the existing EXT4 file system and a state-of-art scalable file system, respectively. 

#### 2. Designing a True Direct-Access File System with DevFS. 
- [Source](https://www.usenix.org/conference/fast18/presentation/kannan) 

##### Abstract 
- We present DevFS, a direct-access file system embedded completely within a storage device. DevFS provides direct access without compromising file system integrity, concurrency, crash consistency, and security. A novel reverse-caching mechanism enables the usage of host memory for inactive objects, thus reducing memory load upon the device.  Evaluation of an emulated DevFS prototype shows more than 2x higher I/O throughput with direct access and up to a 78% reduction in device RAM utilization. 

#### 3. FStream: Managing Flash Streams in the File System. 
- [Source](https://www.usenix.org/conference/fast18/presentation/rho) 

##### Abstract 
- The performance and lifespan of a solid-state drive (SSD) depend not only on the current input workload but also on its internal media fragmentation formed over time. The recently proposed streams gives a means for the host system to control how data are placed on the physical media (abstrated by a stream) and effectively reduce the media fragmentation. This work proposes FStream, a file system approach to taking advantage of this facility. FStream extracts streams at the file system level and avoids complex application level data mapping to streams. Experimental results showed that FStream enhances the filebench performance by 5%-35% and reduces WAF (Write Amplification Factor) by 7%-46%. For a NoSQL database benchmark, 

- performance is improved by up to 38% and WAF 

- is reduced by up to 81%. 

### Distribute and Conquer 

#### 1. Improving Docker Registry Design Based on Production Workload Analysis. 
- [Source](https://www.usenix.org/conference/fast18/presentation/anwar) 

##### Abstract 
- Containers offer an efficient way to run workloads as independent microservices that can be developed, tested and deployed in an agile manner. To facilitate this process, container frameworks offer a registry service that enables users to publish and version container images and share them with others. The registry service plays a critical role in the startup time of containers since many container starts entail the retrieval of container images from a registry. To support research efforts on optimizing the registry service, large-scale and realistic traces are required. In this paper, we perform a comprehensive characterization of a large-scale registry workload based on traces that we collected over the course of 75 days from five IBM data centers hosting production-level registries. We present a trace replayer to perform our analysis and infer a number of crucial insights about container workloads, such as request type distribution, access patterns, and response times. Based on these insights, we derive design implications for the registry and demonstrate their ability to improve performance. Both the traces and the replayer are open-sourced to facilitate further research. 

#### 2. RAID+: Deterministic and Balanced Data Distribution for Large Disk Enclosures. 
- [Source](https://www.usenix.org/conference/fast18/presentation/zhang) 

##### Abstract 
- Existing RAID solutions partition large disk enclosures so that each RAID group uses its own disks exclusively. This achieves good performance isolation across underlying disk groups, at the cost of disk under-utilization and slow RAID reconstruction from disk failures. 

- We propose RAID+, a new RAID construction mechanism that spreads both normal I/O and reconstruction workloads to a larger disk pool in a balanced manner. Unlike systems conducting randomized placement, RAID+ employs deterministic addressing enabled by the mathematical properties of mutually orthogonal Latin squares, based on which it constructs 3-D data templates mapping a logical data volume to uniformly distributed disk blocks across all disks. While the total read/write volume remains unchanged, with or without disk failures, many more disk drives participate in data service and disk reconstruction. Our evaluation with a 60-drive disk enclosure using both synthetic and real-world workloads shows that RAID+ significantly speeds up data recovery while delivering better normal I/O performance and higher multi-tenant system throughput. 

#### 3. Logical Synchronous Replication in the Tintri VMstore File System. 
- [Source](https://www.usenix.org/conference/fast18/presentation/glass) 

##### Abstract 
- A standard feature of enterprise data storage systems is synchronous replication: updates received from clients by one storage system are replicated to a remote storage system and are only acknowledged to clients after having been stored persistently on both storage systems. Traditionally these replication schemes require configuration on a coarse granularity, e.g. on a LUN, filesystem volume, or whole-system basis. In contrast to this, we present a new architecture which operates on a fine granularity---individual files and directories.  To implement this, we use a combination of novel per-file capabilities and existing techniques to solve the following problems: tracking parallel writes in flight on independent storage systems; replicating arbitrary filesystem operations; efficiently resynchronizing after a disconnect; and verifying the integrity of replicated data between two storage systems. 

### Dedup:
Last but Not Least 

#### 1. ALACC: Accelerating Restore Performance of Data Deduplication Systems Using Adaptive Look-Ahead Window Assisted Chunk Caching. 
- [Source](https://www.usenix.org/conference/fast18/presentation/cao) 

##### Abstract 
- Data deduplication has been widely applied in storage systems to improve the efficiency of space utilization. In data deduplication systems, the data restore performance is seriously hindered by read amplification since the accessed data chunks are scattered over many containers. A container consisting of hundreds or thousands data chunks is the data unit to be read from or write to the storage. Several schemes such as forward assembly, container-based caching, and chunk-based caching are used to reduce the number of container-reads during the restore process. However, how to effectively use these schemes to get the best restore performance is still unclear.  

- In this paper, we first study the trade-offs of using these schemes in terms of read amplification and computing time. We then propose a combined data chunk caching and forward assembly scheme called ALACC (Adaptive Look-Ahead Chunk Caching) for improving restore performance which can adapt to different deduplication workloads with a fixed total amount of memory. This is accomplished by extending and shrinking the look-ahead window adaptively to cover an appropriate data recipe range and dynamically deciding the memory to be allocated to forward assembly area and chunk-based caching. Our evaluations show the restore throughput of ALACC is higher than that of the optimum case of various configurations using the fixed amount of memory allocated to forward assembly and to chunk-based caching. 

#### 2. UKSM: Swift Memory Deduplication via Hierarchical and Adaptive Memory Region Distilling. 
- [Source](https://www.usenix.org/conference/fast18/presentation/xia) 

##### Abstract 
- In cloud computing, deduplication can reduce memory footprint by eliminating redundant pages. The responsiveness of a deduplication process to newly generated memory pages is critical. State-of-the-art Content Based Page Sharing (CBPS) approaches lack responsiveness as they equally scan every page while finding redundancies. We propose a new deduplication system UKSM, which prioritizes different memory regions to accelerate the deduplication process and minimize application penalty. With UKSM, memory regions are organized as a distilling hierarchy, where a region in a higher level receives more CPU cycles. UKSM adaptively promotes/demotes a region among levels according to the region’s estimated deduplication benefit and penalty. UKSM further introduces an adaptive partial-page hashing scheme which adjusts a global page hashing strength parameter according to the global degree of page similarity. Experiments demonstrate that, with the same amount of CPU cycles in the same time envelop, UKSM can achieve up to 12.6and 5 more memory saving than CBPS approaches on static and dynamic workloads, respectively. 

