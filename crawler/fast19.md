### Persistent Memory Systems 

#### 1. Reaping the performance of fast NVM storage with uDepot. 
- [Source](https://www.usenix.org/conference/fast19/presentation/kourtis) 

##### Abstract 
- Many applications require low-latency key-value storage, a requirement that is typically satisfied using key-value stores backed by DRAM. Recently, however, storage devices built on novel NVM technologies offer unprecedented performance compared to conventional SSDs. A key-value store that could deliver the performance of these devices would offer many opportunities to accelerate applications and reduce costs. Nevertheless, existing key-value stores, built for slower SSDs or HDDs, cannot fully exploit such devices. 

- In this paper, we present uDepot, a key-value store built bottom-up to deliver the performance of fast NVM block-based devices. uDepot is carefully crafted to avoid inefficiencies, uses a two-level indexing structure that dynamically adjusts its DRAM footprint to match the inserted items, and employs a novel task-based IO run-time system to maximize performance, enabling applications to use fast NVM devices at their full potential. As an embedded store, uDepot's performance nearly matches the raw performance of fast NVM devices both in terms of throughput and latency, while being scalable across multiple devices and cores. As a server, uDepot significantly outperforms state-of-the-art stores that target SSDs under the YCSB benchmark. Finally, using a Memcache service on top of uDepot we demonstrate that data services built on NVM storage devices can offer equivalent performance to their DRAM-based counterparts at a much lower cost. Indeed, using uDepot we have built a cloud Memcache service that is currently available as an experimental offering in the public cloud. 

#### 2. Optimizing Systems for Byte-Addressable NVM by Reducing Bit Flipping. 
- [Source](https://www.usenix.org/conference/fast19/presentation/bittman) 

##### Abstract 
- New byte-addressable non-volatile memory (BNVM) technologies such as phase change memory (PCM) enable the construction of systems with large persistent memories, improving reliability and potentially reducing power consumption. However, BNVM technologies only support a limited number of lifetime writes per cell and consume most of their power when flipping a bit's state during a write; thus, PCM controllers only rewrite a cell's contents when the cell's value has changed. Prior research has assumed that reducing the number of words written is a good proxy for reducing the number of bits modified, but a recent study has suggested that this assumption may not be valid. Our research confirms that approaches with the fewest writes often have more bit flips than those optimized to reduce bit flipping. 

- To test the effectiveness of bit flip reduction, we built a framework that uses the number of bits flipped over time as the measure of "goodness" and modified a cycle-accurate simulator to count bits flipped during program execution. We implemented several modifications to common data structures designed to reduce power consumption and increase memory lifetime by reducing the number of bits modified by operations on several data structures: linked lists, hash tables, and red-black trees. We were able to reduce the number of bits flipped by up to 3.56× over standard implementations of the same data structures with negligible overhead. We measured the number of bits flipped by memory allocation and stack frame saves and found that careful data placement in the stack can reduce bit flips significantly. These changes require no hardware modifications and neither significantly reduce performance nor increase code complexity, making them attractive for designing systems optimized for BNVM. 

#### 3. Write-Optimized Dynamic Hashing for Persistent Memory. 
- [Source](https://www.usenix.org/conference/fast19/presentation/nam) 

##### Abstract 
- Low latency storage media such as byte-addressable persistent memory (PM) requires rethinking of various data structures in terms of optimization. One of the main challenges in implementing hash-based indexing structures on PM is how to achieve efficiency by making effective use of cachelines while guaranteeing failure-atomicity for dynamic hash expansion and shrinkage. In this paper, we present Cacheline-Conscious Extendible Hashing (CCEH) that reduces the overhead of dynamic memory block management while guaranteeing constant hash table lookup time. CCEH guarantees failure-atomicity without making use of explicit logging. Our experiments show that CCEH effectively adapts its size as the demand increases under the fine-grained failure-atomicity constraint and reduces the maximum query latency by over two-thirds compared to the state-of-the-art hashing techniques. 

#### 4. Software Wear Management for Persistent Memories. 
- [Source](https://www.usenix.org/conference/fast19/presentation/gogte) 

##### Abstract 
- The commercial release of byte-addressable persistent memories (PMs) is imminent. Unfortunately, these devices suffer from limited write endurance—without any wear management, PM lifetime might be as low as 1.1 months. Existing wear-management techniques introduce an additional indirection layer to remap memory across physical frames and require hardware support to track fine-grain wear. These mechanisms incur storage overhead and increase access latency and energy consumption. 

- We present Kevlar, an OS-based wear-management technique for PM that requires no new hardware. Kevlar uses existing virtual memory mechanisms to remap pages, enabling it to perform both wear leveling—shuffling pages in PM to even wear; and wear reduction—transparently migrating heavily written pages to DRAM. Crucially, Kevlar avoids the need for hardware support to track wear at fine grain. Instead, it relies on a novel wear estimation technique that builds upon Intel's Precise Event Based Sampling to approximately track processor cache contents via a software-maintained Bloom filter and estimate write-back rates at fine grain. We implement Kevlar in Linux and demonstrate that it achieves lifetime improvement of 18.4x (avg.) over no wear management while incurring 1.2% performance overhead. 

### File Systems 

#### 1. Storage Gardening: Using a Virtualization Layer for Efficient Defragmentation in the WAFL File System. 
- [Source](https://www.usenix.org/conference/fast19/presentation/kesavan) 

##### Abstract 
- As a file system ages, it can experience multiple forms of fragmentation. Fragmentation of the free space in the file system can lower write performance and subsequent read performance. Client operations as well as internal operations, such as deduplication, can fragment the layout of an individual file, which also impacts file read performance. File systems that allow sub-block granular addressing can gather intra-block fragmentation, which leads to wasted free space. This paper describes how the NetApp® WAFL® file system leverages a storage virtualization layer for defragmentation techniques that physically relocate blocks efficiently, including those in read-only snapshots. The paper analyzes the effectiveness of these techniques at reducing fragmentation and improving overall performance across various storage media. 

#### 2. Pay Migration Tax to Homeland: Anchor-based Scalable Reference Counting for Multicores. 
- [Source](https://www.usenix.org/conference/fast19/presentation/jung) 

##### Abstract 
- The operating system community has been combating scalability bottlenecks for the past 10 years with victories or all the then-new multicore hardware. File systems, however, are in the midst of turmoil yet. One of the culprits behind performance degradation is reference counting widely used for managing data and metadata, and scalability is badly impacted under load with little or no logical contention, where the capability is desperately needed. To address this, we propose PAYGO, a reference counting technique that combines per-core hash of local reference counters with an anchor counter to make concurrent counting scalable as well as space-efficient, without having any other delay for managing counters. PAYGO imposes the restriction that decrement must be performed on the original local counter where the act of increment has occurred so that reclaiming zero-valued local counters can be done immediately. To this end, we enforce migrated processes running on different cores to update the anchor counter associated with the original local counter. We implemented PAYGO in the Linux page cache, and so our implementation is transparent to the file system. Experimental evaluation with underlying file systems (i.e., ext4, F2FS, btrfs, and XFS) demonstrated that PAYGO scales file systems better than other state-of-the-art techniques. 

#### 3. Speculative Encryption on GPU Applied to Cryptographic File Systems. 
- [Source](https://www.usenix.org/conference/fast19/presentation/eduardo) 

##### Abstract 
- Due to the processing of cryptographic functions, Cryptographic File Systems (CFSs) may require significant processing capacity. Parallel processing techniques on CPUs or GPUs can be used to meet this demand. The CTR mode has two particularly useful features: the ability to be fully parallelizable and to perform the initial step of the encryption process ahead of time, generating encryption masks. This work presents an innovative approach in which the CTR mode is applied in the context of CFSs seeking to exploit these characteristics, including the anticipated production of the cipher masks (speculative encryption) in GPUs. Techniques that demonstrate how to deal with the issue of the generation, storage and management of nonces are presented, an essential component to the operation of the CTR mode in the context of CFSs. Related to GPU processing, our methods work to perform the handling of the encryption contexts and control the production of the masks, aiming to produce them with the adequate anticipation and overcome the extra latency due to encryption tasks. The techniques were applied in the implementation of EncFS++, a user space CFS. Performance analyzes showed that it was possible to achieve significant gains in throughput and CPU efficiency in several scenarios. They also demonstrated that GPU processing can be efficiently applied to CFS encryption workload even when working by encrypting small amounts of data (4 KiB), and in scenarios where higher speed/lower latency storage devices are used, such as SSDs or memory. 

### Deduplication 

#### 1. Sketching Volume Capacities in Deduplicated Storage. 
- [Source](https://www.usenix.org/conference/fast19/presentation/harnik) 

##### Abstract 
- The adoption of deduplication in storage systems has introduced significant new challenges for storage management. Specifically, the physical capacities associated with volumes are no longer readily available. In this work we introduce a new approach to analyzing capacities in deduplicated storage environments. We provide sketch-based estimations of fundamental capacity measures required for managing a storage system: How much physical space would be reclaimed if a volume or group of volumes were to be removed from a system (the {\em reclaimable} capacity) and how much of the physical space should be attributed to each of the volumes in the system (the {\em attributed} capacity). Our methods also support capacity queries for volume groups across multiple storage systems, e.g., how much capacity would a volume group consume after being migrated to another storage system? We provide analytical accuracy guarantees for our estimations as well as empirical evaluations. Our technology is integrated into a prominent all-flash storage array and exhibits high performance even for very large systems. We also demonstrate how this method opens the door for performing placement decisions at the data center level and obtaining insights on deduplication in the field. 

#### 2. Finesse: Fine-Grained Feature Locality based Fast Resemblance Detection for Post-Deduplication Delta Compression. 
- [Source](https://www.usenix.org/conference/fast19/presentation/zhang) 

##### Abstract 
- In storage systems, delta compression is often used as a complementary data reduction technique for data deduplication because it is able to eliminate redundancy among the non-duplicate but highly similar chunks. Currently, what we call  

#### 3. Sliding Look-Back Window Assisted Data Chunk Rewriting for Improving Deduplication Restore Performance. 
- [Source](https://www.usenix.org/conference/fast19/presentation/cao) 

##### Abstract 
- Data deduplication is an effective way of improving storage space utilization. The data generated by deduplication is persistently stored in data chunks or data containers (a container consisting of a few hundreds or thousands of data chunks). The data restore process is rather slow due to data fragmentation and read amplification. To speed up the restore process, data chunk rewrite (a rewrite is to store a duplicate data chunk) schemes have been proposed to effectively improve data chunk locality and reduce the number of container reads for restoring the original data. However, rewrites will decrease the deduplication ratio since more storage space is used to store the duplicate data chunks. 

- To remedy this, we focus on reducing the data fragmentation and read amplification of container-based deduplication systems. We first propose a flexible container referenced count based rewrite scheme, which can make a better tradeoff between the deduplication ratio and the number of required container reads than that of capping which is an existing rewrite scheme. To further improve the rewrite candidate selection accuracy, we propose a sliding look-back window based design, which can make more accurate rewrite decisions by considering the caching effect, data chunk localities, and data chunk closeness in the current and future windows. According to our evaluation, our proposed approach can always achieve a higher restore performance than that of capping especially when the reduction of deduplication ratio is small. 

### Storage Potpourri 

#### 1. DistCache: Provable Load Balancing for Large-Scale Storage Systems with Distributed Caching. 
- [Source](https://www.usenix.org/conference/fast19/presentation/liu) 

##### Abstract 
- Load balancing is critical for distributed storage to meet strict service-level objectives (SLOs). It has been shown that a fast cache can guarantee load balancing for a clustered storage system. However, when the system scales out to multiple clusters, the fast cache itself would become the bottleneck. Traditional mechanisms like cache partition and cache replication either result in load imbalance between cache nodes or have high overhead for cache coherence. 

- We present DistCache, a new distributed caching mechanism that provides provable load balancing for large-scale storage systems. DistCache co-designs cache allocation with cache topology and query routing. The key idea is to partition the hot objects with independent hash functions between cache nodes in different layers, and to adaptively route queries with the power-of-two-choices. We prove that DistCache enables the cache throughput to increase linearly with the number of cache nodes, by unifying techniques from expander graphs, network flows, and queuing theory. DistCache is a general solution that can be applied to many storage systems. We demonstrate the benefits of DistCache by providing the design, implementation, and evaluation of the use case for emerging switch-based caching. 

#### 2. GearDB: A GC-free Key-Value Store on HM-SMR Drives with Gear Compaction. 
- [Source](https://www.usenix.org/conference/fast19/presentation/yao) 

##### Abstract 
- Host-managed shingled magnetic recording drives (HM-SMR) give a capacity advantage to harness the explosive growth of data. Applications where data is sequentially written and randomly read make the HM-SMR an ideal solution due to its capacity, predictable performance, and economical cost. Key-value stores based on the Log-Structured Merge Trees (LSM-trees) data structure is such a good fit due to their batched sequential writes. However, building an LSM-tree based KV store on HM-SMR drives presents severe challenges in maintaining the performance and space efficiency due to the redundant cleaning processes for applications and storage devices (i.e., compaction and garbage collections). To eliminate the overhead of on-disk garbage collections (GC) and improve compaction efficiency, this paper presents GearDB, a GC-free KV store tailored for HM-SMR drives, with three new techniques: a new on-disk data layout, compaction windows, and a novel gear compaction algorithm. We implement GearDB and evaluate it with LevelDB on a real HM-SMR drive. Our extensive experiments have shown that GearDB achieves good performance and space efficiency, i.e., on average $1.71\times$ faster than LevelDB in random write with a space efficiency of 89.9%. 

#### 3. SPEICHER: Securing LSM-based Key-Value Stores using Shielded Execution. 
- [Source](https://www.usenix.org/conference/fast19/presentation/bailleu) 

##### Abstract 
- We introduce Speicher, a secure storage system that not only provides strong confidentiality and integrity properties, but also ensures data freshness to protect against rollback/forking attacks. Speicher exports a Key-Value (KV) interface backed by Log-Structured Merge Tree (LSM) for supporting secure data storage and query operations. Speicher enforces these security properties on an untrusted host by leveraging shielded execution based on a hardware-assisted trusted execution environment (TEE)—specifically, Intel SGX. However, the design of Speicher extends the trust in shielded execution beyond the secure SGX enclave memory region to ensure that the security properties are also preserved in the stateful (or non-volatile) setting of an untrusted storage medium, including system crash, reboot, or migration. 

- More specifically, we have designed an authenticated and confidentiality-preserving LSM data structure. We have further hardened the LSM data structure to ensure data freshness by designing asynchronous trusted counters. Lastly, we designed a direct I/O library for shielded execution based on Intel SPDK to overcome the I/O bottlenecks in the SGX enclave. We have implemented Speicher as a fully-functional storage system by extending RocksDB, and evaluated its performance using the RocksDB benchmark. Our experimental evaluation shows that Speicher incurs reasonable overheads for providing strong security guarantees, while keeping the trusted computing base (TCB) small. 

### NVM File and Storage Systems 

#### 1. SLM-DB: Single-Level Key-Value Store with Persistent Memory. 
- [Source](https://www.usenix.org/conference/fast19/presentation/kaiyrakhmet) 

##### Abstract 
- This paper investigates how to leverage emerging byte-addressable persistent memory (PM) to enhance the performance of key-value (KV) stores. We present a novel KV store, the Single-Level Merge DB (SLM-DB), which takes advantage of both the B+-tree index and the Log-Structured Merge Trees (LSM-tree) approach by making the best use of fast persistent memory. Our proposed SLM-DB achieves high read performance as well as high write performance with low write amplification and near-optimal read amplification. In SLM-DB, we exploit persistent memory to maintain a B+-tree index and adopt an LSM-tree approach to stage inserted KV pairs in a PM resident memory buffer. SLM-DB has a single-level organization of KV pairs on disks and performs selective compaction for the KV pairs, collecting garbage and keeping the KV pairs sorted sufficiently for range query operations. Our extensive experimental study demonstrates that, in our default setup, compared to LevelDB, SLM-DB provides 1.07 - 1.96 and 1.56 - 2.22 times higher read and write throughput, respectively, as well as comparable range query performance. 

#### 2. Ziggurat: A Tiered File System for Non-Volatile Main Memories and Disks. 
- [Source](https://www.usenix.org/conference/fast19/presentation/zheng) 

##### Abstract 
- Emerging fast, byte-addressable Non-Volatile Main Memory (NVMM) provides huge increases in storage performance compared to traditional disks. We present Ziggurat, a tiered file system that combines NVMM and slow disks to create a storage system with near-NVMM performance and large capacity. Ziggurat steers incoming writes to NVMM, DRAM, or disk depending on application access patterns, write size, and the likelihood that the application will stall until the write completes. Ziggurat profiles the application's access stream online to predict the behavior of individual writes. In the background, Ziggurat estimates the "temperature" of file data, and migrates the cold file data from NVMM to disks. To fully utilize disk bandwidth, Ziggurat coalesces data blocks into large, sequential writes. Experimental results show that with a small amount of NVMM and a large SSD, Ziggurat achieves up to 38.9x and 46.5x throughput improvement compared with EXT4 and XFS running on an SSD alone, respectively. As the amount of NVMM grows, Ziggurat's performance improves until it matches the performance of an NVMM-only file system. 

#### 3. Orion: A Distributed File System for Non-Volatile Main Memory and RDMA-Capable Networks. 
- [Source](https://www.usenix.org/conference/fast19/presentation/yang) 

##### Abstract 
- High-performance, byte-addressable non-volatile main memories (NVMMs) force system designers to rethink trade-offs throughout the system stack, often leading to dramatic changes in system architecture. Conventional distributed file systems are a prime example. When faster NVMM replaces block-based storage, the dramatic improvement in storage performance makes networking and software overhead a critical bottleneck. 

- In this paper, we present Orion, a distributed file system for NVMM-based storage. By taking a clean slate design and leveraging the characteristics of NVMM and high-speed, RDMA-based networking, Orion provides high-performance metadata and data access while maintaining the byte addressability of NVMM. Our evaluation shows Orion achieves performance comparable to local NVMM file systems and outperforms existing distributed file systems by a large margin. 

### Big Systems 

#### 1. INSTalytics: Cluster Filesystem Co-design for Big-data Analytics. 
- [Source](https://www.usenix.org/conference/fast19/presentation/sivathanu) 

##### Abstract 
- We present the design, implementation, and evaluation of Instalytics, a co-designed stack of a cluster file system and the compute layer, for efficient big data analytics in large-scale data centers. Instalytics amplifies the well-known benefits of data partitioning in analytics systems; instead of traditional partitioning on one dimension, Instalytics enables data to be simultaneously partitioned on four different dimensions at the same storage cost, enabling a larger fraction of queries to benefit from partition filtering and joins without network shuffle. 

- To achieve this, Instalytics uses compute-awareness to customize the 3-way replication that the cluster file system employs for availability. A new heterogeneous replication layout enables Instalytics to preserve the same recovery cost and availability as traditional replication. Instalytics also uses compute-awareness to expose a new {\em sliced-read} API that improves performance of joins by enabling multiple compute nodes to read slices of a data block efficiently via co-ordinated request scheduling and selective caching at the storage nodes. 

- We have implemented Instalytics in a production analytics stack, and show that recovery performance and availability is similar to physical replication, while providing significant improvements in query performance, suggesting a new approach to designing cloud-scale big-data analytics systems. 

#### 2. GraphOne: A Data Store for Real-time Analytics on Evolving Graphs. 
- [Source](https://www.usenix.org/conference/fast19/presentation/kumar) 

##### Abstract 
- There is a growing need to perform real-time analytics on evolving graphs in order to deliver the values of big data to users. The key requirement from such applications is to have a data store to support their diverse data access efficiently, while concurrently ingesting fine-grained updates at a high velocity. Unfortunately, current graph systems, either graph databases or analytics engines, are not designed to achieve high performance for both operations. To address this challenge, we have designed and developed GraphOne, a graph data store that combines two complementary graph storage formats (edge list and adjacency list), and uses dual versioning to decouple graph computations from updates. Importantly, it presents a new data abstraction, GraphView, to enable data access at two different granularities with only a small data duplication. Experimental results show that GraphOne achieves an ingestion rate of two to three orders of magnitude higher than graph databases, while delivering algorithmic performance comparable to a static graph system. GraphOne is able to deliver 5.36x higher update rate and over 3x better analytics performance compared to a state-of-the-art dynamic graph system. 

#### 3. Automatic, Application-Aware I/O Forwarding Resource Allocation. 
- [Source](https://www.usenix.org/conference/fast19/presentation/ji) 

##### Abstract 
- The I/O forwarding architecture is widely adopted on modern supercomputers, with a layer of intermediate nodes sitting between the many compute nodes and backend storage nodes. This allows compute nodes to run more efficiently and stably with a leaner OS, offloads I/O coordination and communication with backend from the compute nodes, maintains less concurrent connections to storage systems, and provides additional resources for effective caching, prefetching, write buffering, and I/O aggregation. However, with many existing machines, these forwarding nodes are assigned to serve fixed set of compute nodes. 

- We explore an automatic mechanism, DFRA, for application-adaptive dynamic forwarding resource allocation. With I/O monitoring data that proves affordable to acquire in real time and maintain for long-term history analysis, Upon each job's dispatch, DFRA conducts a history-based study to determine whether the job should be granted more forwarding resources or given dedicated forwarding nodes. Such customized I/O forwarding lets the small fraction of I/O-intensive applications achieve higher I/O performance and scalability, meanwhile effectively isolating disruptive I/O activities. We implemented, evaluated, and deployed DFRA on Sunway TaihuLight, the current No.2 supercomputer in the world. It improves applications' I/O performance by up to 16.0x, eliminates most of the inter-application I/O interference, and has saved over 200 million of core-hours during its deployment on TaihuLight for past 8 months. Finally, our proposed DFRA design is not platform-dependent, making it applicable to the management of existing and future I/O forwarding or burst buffer resources. 

### Flash and Emerging Storage Systems 

#### 1. Design Tradeoffs for SSD Reliability. 
- [Source](https://www.usenix.org/conference/fast19/presentation/kim-bryan) 

##### Abstract 
- Flash memory-based SSDs are popular across a wide range of data storage markets, while the underlying storage medium—flash memory—is becoming increasingly unreliable. As a result, modern SSDs employ a number of in-device reliability enhancement techniques, but none of them offers a one size fits all solution when considering the multi-dimensional requirements for SSDs: performance, reliability, and lifetime. In this paper, we examine the design tradeoffs of existing reliability enhancement techniques such as data re-read, intra-SSD redundancy, and data scrubbing. We observe that an uncoordinated use of these techniques adversely affects the performance of the SSD, and careful management of the techniques is necessary for a graceful performance degradation while maintaining a high reliability standard. To that end, we propose a holistic reliability management scheme that selectively employs redundancy, conditionally re-reads, judiciously selects data to scrub. We demonstrate the effectiveness of our scheme by evaluating it across a set of I/O workloads and SSDs wear states. 

#### 2. Fully Automatic Stream Management for Multi-Streamed SSDs Using Program Contexts. 
- [Source](https://www.usenix.org/conference/fast19/presentation/kim-taejin) 

##### Abstract 
- Multi-streamed SSDs can significantly improve both the performance and lifetime of flash-based SSDs when their streams are properly managed. However, existing stream management solutions do not adequately support the multi-streamed SSDs for their wide adoption. No existing stream management technique works in a fully automatic fashion for general I/O workloads. Furthermore, the limited number of available streams makes it difficult to effectively manage streams when a large number of streams are required. In this paper, we propose a fully automatic stream management technique, PCStream, which can work efficiently for general I/O workloads with heterogeneous write characteristics. PCStream is based on the key insight that stream allocation decisions should be made on dominant I/O activities. By identifying dominant I/O activities using program contexts, PCStream fully automates the whole process of stream allocation within the kernel with no manual work. In order to overcome the limited number of supported streams, we propose a new type of streams, internal streams, which can be implemented at low cost. PCStream can effectively double the number of available streams using internal streams. Our evaluations on real multi-streamed SSDs show that PCStream achieves the same efficiency as highly-optimized manual allocations by experienced programmers. PCStream improves IOPS by up to 56% over the existing automatic technique by reducing the garbage collection overhead by up to 69%. 

#### 3. Large-Scale Graph Processing on Emerging Storage Devices. 
- [Source](https://www.usenix.org/conference/fast19/presentation/elyasi) 

##### Abstract 
- Graph processing is becoming commonplace in many applications to analyze huge datasets. Much of the prior work in this area has assumed I/O devices with considerable latencies, especially for random accesses, using large amount of DRAM to trade-off additional computation for I/O accesses. However, emerging storage devices, including currently popular SSDs, provide fairly comparable sequential and random accesses, making these prior solutions inefficient. In this paper, we point out this inefficiency, and propose a new graph partitioning and processing framework to leverage these new device capabilities. We show experimentally on an actual platform that our proposal can give 2X better performance than a state-of-the-art solution. 

### Erasure Coding and Reliability 

#### 1. Fast Erasure Coding for Data Storage: A Comprehensive Study of the Acceleration Techniques. 
- [Source](https://www.usenix.org/conference/fast19/presentation/zhou) 

##### Abstract 
- Various techniques have been proposed in the literature to improve erasure code computation efficiency, including optimizing bitmatrix design, optimizing computation schedule, common XOR operation reduction, caching management techniques, and vectorization techniques. These techniques were largely proposed individually previously, and in this work, we seek to use them jointly. In order to accomplish this task, these techniques need to be thoroughly evaluated individually, and their relation better understood. Building on extensive test results, we develop methods to systematically optimize the computation chain together with the underlying bitmatrix. This led to a simple design approach of optimizing the bitmatrix by minimizing a weighted cost function, and also a straightforward erasure coding procedure: use the given bitmatrix to produce the computation schedule, which utilizes both the XOR reduction and caching management techniques, and apply XOR level vectorization. This procedure can provide a better performance than most existing techniques, and even compete against well-known codes such as EVENODD, RDP, and STAR codes. Moreover, the result suggests that vectorizing the XOR operation is a better choice than directly vectorizing finite field operations, not only because of the better encoding throughput, but also its minimal migration efforts onto newer CPUs. 

#### 2. OpenEC: Toward Unified and Configurable Erasure Coding Management in Distributed Storage Systems. 
- [Source](https://www.usenix.org/conference/fast19/presentation/li) 

##### Abstract 
- Erasure coding becomes a practical redundancy technique for distributed storage systems to achieve fault tolerance with low storage overhead. Given its popularity, research studies have proposed theoretically proven erasure codes or efficient repair algorithms to make erasure coding more viable. However, integrating new erasure coding solutions into existing distributed storage systems is a challenging task and requires non-trivial re-engineering of the underlying storage workflows. We present OpenEC, a unified and configurable framework for readily deploying a variety of erasure coding solutions into existing distributed storage systems. OpenEC decouples erasure coding management from the storage workflows of distributed storage systems, and provides erasure coding designers with configurable controls of erasure coding operations through a directed-acyclic-graph-based programming abstraction. We prototype OpenEC on two versions of HDFS with limited code modifications. Experiments on a local cluster and Amazon EC2 show that OpenEC preserves both the operational performance and the properties of erasure coding solutions; OpenEC can also automatically optimize erasure coding operations to improve repair performance. 

#### 3. Cluster storage systems gotta have HeART: improving storage efficiency by exploiting disk-reliability heterogeneity. 
- [Source](https://www.usenix.org/conference/fast19/presentation/kadekodi) 

##### Abstract 
- Large-scale cluster storage systems typically consist of a heterogeneous mix of storage devices with significantly varying failure rates. Despite such differences among devices, redundancy settings are generally configured in a one-scheme-for-all fashion. In this paper, we make a case for exploiting reliability heterogeneity to tailor redundancy settings to different device groups. We present HeART, an online tuning tool that guides selection of, and transitions between redundancy settings for long-term data reliability, based on observed reliability properties of each disk group. By processing disk failure data over time, HeART identifies the boundaries and steady-state failure rate for each deployed disk group (e.g., by make/model). Using this information, HeART suggests the most space-efficient redundancy option allowed that will achieve the specified target data reliability. Analysis of longitudinal failure data for a large production storage cluster shows the robustness of HeART's failure-rate determination algorithms. The same analysis shows that a storage system guided by HeART could provide target data reliability levels with fewer disks than one-scheme-for-all approaches: 11–16% fewer compared to erasure codes like 10-of-14 or 6-of-9 and 33% fewer compared to 3-way replication. 

#### 4. ScaleCheck: A Single-Machine Approach for Discovering Scalability Bugs in Large Distributed Systems. 
- [Source](https://www.usenix.org/conference/fast19/presentation/stuardo) 

##### Abstract 
- We present ScaleCheck, an approach for discovering scalability bugs (a new class of bug in large storage systems) and for democratizing large-scale testing. ScaleCheck employs a program analysis technique, for finding potential causes of scalability bugs, and a series of colocation techniques, for testing implementation code at real scales but doing so on just a commodity PC. ScaleCheck has been integrated to several large-scale storage systems, Cassandra, HDFS, Riak, and Voldemort, and successfully exposed known and unknown scalability bugs, up to 512-node scale on a 16-core PC. 

