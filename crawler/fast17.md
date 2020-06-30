### Garbage 

#### 1. Algorithms and Data Structures for Efficient Free Space Reclamation in WAFL. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/kesavan) 

##### Abstract 
- NetApp®WAFL®is a transactional file system that uses the copy-on-write mechanism to support fast write performance and efficient snapshot creation. However, copy-on-write increases the demand on the file system to find free blocks quickly; failure to do so may impede allocations for incoming writes. Efficiency is also important, because the task may consume CPU and other resources. In this paper, we describe the evolution (over more than a decade) of WAFL’s algorithms and data structures for reclaiming space with minimal impact on the overall storage appliance performance. 

#### 2. Tiny-Tail Flash: Near-Perfect Elimination of Garbage Collection Tail Latencies in NAND SSDs. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/yan) 

##### Abstract 
- TTFLASH is a “tiny-tail” flash drive (SSD) that eliminates GC-induced tail latencies by circumventing GCblocked I/Os with four novel strategies: plane-blocking GC, rotating GC, GC-tolerant read, and GC-tolerant flush. It is built on three SSD internal advancements: powerful controllers, parity-based RAIN, and capacitorbacked RAM, but is dependent on the use of intra-plane copyback operations. We show that TTFLASH comes significantly close to a “no-GC” scenario. Specifically, between 99–99.99th percentiles, TTFLASH is only 1.0 to 2.6× slower than the no-GC case, while a base approach suffers from 5–138× GC-induced slowdowns. 

#### 3. The Logic of Physical Garbage Collection in Deduplicating Storage. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/douglis) 

##### Abstract 
- Most storage systems that write in a log-structured manner need a mechanism for garbage collection (GC), reclaiming and consolidating space by identifying unused areas on disk. In a deduplicating storage system, GC is complicated by the possibility of numerous references to the same underlying data. We describe two variants of garbage collection in a commercial deduplicating storage system, a logical GC that operates on the files containing deduplicated data and a physical GC that performs sequential I/O on the underlying data. The need for the second approach arises from a shift in the underlying workloads, in which exceptionally high duplication ratios or the existence of millions of individual small files result in unacceptably slow GC using the file-level approach. Under such workloads, determining the liveness of chunks becomes a slow phase of logical GC. We find that physical GC decreases the execution time of this phase by up to two orders of magnitude in the case of extreme workloads and improves it by approximately 10–60% in the common case, but only after additional optimizations to compensate for its higher initialization overheads. 

### The System 

#### 1. File Systems Fated for Senescence? Nonsense, Says Science! 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/conway) 

##### Abstract 
- File systems must allocate space for files without knowing what will be added or removed in the future. Over the life of a file system, this may cause suboptimal file placement decisions which eventually lead to slower performance, or  

-  However, this paper describes realistic as well as synthetic workloads that can cause these heuristics to fail, inducing large performance declines due to aging. For example, on ext4 and ZFS, a few hundred git pull operations can reduce read performance by a factor of 2; performing a thousand pulls can reduce performance by up to a factor of 30. We further present microbenchmarks demonstrating that common placement strategies are extremely sensitive to file-creation order; varying the creation order of a few thousand small files in a real-world directory structure can slow down reads by 15–175x, depending on the file system. 

-  We argue that these slowdowns are caused by poor layout. We demonstrate a correlation between read performance of a directory scan and the locality within a file system’s access patterns, using a  

- In short, many file systems are exquisitely prone to read aging for a variety of write workloads. We show, however, that aging is not inevitable. BetrFS, a file system based on write-optimized dictionaries, exhibits almost no aging in our experiments. BetrFS typically outperforms the other file systems in our benchmarks; aged BetrFS even outperforms the unaged versions of these file systems, excepting Btrfs. We present a framework for understanding and predicting aging, and identify the key features of BetrFS that avoid aging. 

#### 2. To FUSE or Not to FUSE: Performance of User-Space File Systems. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/vangoor) 

##### Abstract 
- Traditionally, file systems were implemented as part of OS kernels. However, as complexity of file systems grew, many new file systems began being developed in user space. Nowadays, user-space file systems are often used to prototype and evaluate new approaches to file system design. Low performance is considered the main disadvantage of user-space file systems but the extent of this problem has never been explored systematically. As a result, the topic of user-space file systems remains rather controversial: while some consider user-space file systems a toy not to be used in production, others develop full-fledged production file systems in user space. In this paper we analyze the design and implementation of the most widely known user-space file system framework—FUSE—and characterize its performance for a wide range of workloads. We instrumented FUSE to extract useful statistics and traces, which helped us analyze its performance bottlenecks and present our analysis results. Our experiments indicate that depending on the workload and hardware used, performance degradation caused by FUSE can be completely imperceptible or as high as –83% even when optimized; and relative CPU utilization can increase by 31%. 

#### 3. Knockoff: Cheap Versions in the Cloud. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/dou) 

##### Abstract 
- Cloud-based storage provides reliability and ease-of-management. Unfortunately, it can also incur significant costs for both storing and communicating data, even after using techniques such as chunk-based deduplication and delta compression. The current trend of providing access to past versions of data exacerbates both costs. 

- In this paper, we show that deterministic recomputation of data can substantially reduce the cost of cloud storage. Borrowing a well-known dualism from the fault-tolerance community, we note that any data can be equivalently represented by a log of the nondeterministic inputs needed to produce that data. We design a file system, called Knockoff, that selectively substitutes nondeterministic inputs for file data to reduce communication and storage costs. Knockoff compresses both data and computation logs: it uses chunk-based deduplication for file data and delta compression for logs of nondeterminism. In two studies, Knockoff reduces the average cost of sending files to the cloud without versioning by 21% and 24%; the relative benefit increases as versions are retained more frequently. 

#### 4. HopsFS: Scaling Hierarchical File System Metadata Using NewSQL Databases. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/niazi) 

##### Abstract 
- Recent improvements in both the performance and scalability of shared-nothing, transactional, in-memory NewSQL databases have reopened the research question of whether distributed metadata for hierarchical file systems can be managed using commodity databases. In this paper, we introduce HopsFS, a next generation distribution of the Hadoop Distributed File System (HDFS) that replaces HDFS’ single node in-memory metadata service, with a distributed metadata service built on a NewSQL database. By removing the metadata bottleneck, HopsFS enables an order of magnitude larger and higher throughput clusters compared to HDFS. Metadata capacity has been increased to at least 37 times HDFS’ capacity, and in experiments based on a workload trace from Spotify, we show that HopsFS supports 16 to 37 times the throughput of Apache HDFS. HopsFS also has lower latency for many concurrent clients, and no downtime during failover. Finally, as metadata is now stored in a commodity database, it can be safely extended and easily exported to external systems for online analysis and free-text search. 

### Edward Sharpe and the Magnetic Zeros 

#### 1. Evolving Ext4 for Shingled Disks. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/aghayev) 

##### Abstract 
- Drive-Managed SMR (ShingledMagnetic Recording) disks offer a plug-compatible higher-capacity replacement for conventional disks. For non-sequential workloads, these disks show bimodal behavior: After a short period of high throughput they enter a continuous period of low throughput. 

- We introduce ext4-lazy 

#### 2. SMaRT: An Approach to Shingled Magnetic Recording Translation. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/he) 

##### Abstract 
- Shingled Magnetic Recording (SMR) is a new technique for increasing areal data density in hard drives. Drivemanaged SMR (DM-SMR) drives employ a shingled translation layer to mask internal data management and support block interface to the host software. Two major challenges of designing an efficient shingled translation layer for DM-SMR drives are metadata overhead and garbage collection overhead.  

- In this paper we introduce SMaRT, an approach to  

- We implement SMaRT and compare it with a regular Hard Disk Drive (HDD) and a simulated Seagate DM-SMR drive. The experiments with several block I/O traces demonstrate that SMaRT performs better than the Seagate drive and even provides comparable performance as regular HDDs when drive space usage is below a certain threshold. 

#### 3. Facilitating Magnetic Recording Technology Scaling for Data Center Hard Disk Drives through Filesystem-Level Transparent Local Erasure Coding. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/li) 

##### Abstract 
- This paper presents a simple yet effective design solution to facilitate technology scaling for hard disk drives (HDDs) being deployed in data centers. Emerging magnetic recording technologies improve storage areal density mainly through reducing the track pitch, which however makes HDDs subject to higher read retry rates. More frequent HDD read retries could cause intolerable tail latency for large-scale systems such as data centers. To reduce the occurrence of costly read retry, one intuitive solution is to apply erasure coding locally on each HDD or JBOD (just a bunch of disks). To be practically viable, local erasure coding must have very low coding redundancy, which demands very long codeword length (e.g., one codeword spans hundreds of 4kB sectors) and hence large file size. This makes local erasure coding mainly suitable for data center applications. This paper contends that local erasure coding should be implemented transparently within filesystems, and accordingly presents a basic design framework and elaborates on important design issues. Meanwhile, this paper derives the mathematical formulations for estimating its effect on reducing HDD read tail latency. Using Reed-Solomon (RS) based erasure codes as test vehicles, we carried out detailed analysis and experiments to evaluate its implementation feasibility and effectiveness. We integrated the developed design solution into ext4 to further demonstrate its feasibility and quantitatively measure its impact on average speed performance of various big data benchmarks. 

### Corruption 

#### 1. Redundancy Does Not Imply Fault Tolerance: Analysis of Distributed Storage Reactions to Single Errors and Corruptions. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/ganesan) 

##### Abstract 
- We analyze how modern distributed storage systems behave in the presence of file-system faults such as data corruption and read and write errors. We characterize eight popular distributed storage systems and uncover numerous bugs related to file-system fault tolerance. We find that modern distributed systems do not consistently use redundancy to recover from file-system faults: a single file-system fault can cause catastrophic outcomes such as data loss, corruption, and unavailability. Our results have implications for the design of next generation fault-tolerant distributed and cloud storage systems. 

#### 2. Omid, Reloaded: Scalable and Highly-Available Transaction Processing. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/shacham) 

##### Abstract 
- We present Omid—a transaction processing service that powers web-scale production systems at Yahoo. Omid provides ACID transaction semantics on top of traditional key-value storage; its implementation over Apache HBase is open sourced as part of Apache Incubator. Omid can serve hundreds of thousands of transactions per second on standard mid-range hardware, while incurring minimal impact on the speed of data access in the underlying key-value store. Additionally, as expected from always-on production services, Omid is highly available. 

#### 3. Application Crash Consistency and Performance with CCFS. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/pillai) 

##### Abstract 
- Recent research has shown that applications often incorrectly implement crash consistency. We present ccfs, a file system that improves the correctness of application-level crash consistency protocols while maintaining high performance. A key idea in ccfs is the abstraction of a  

#### 4. High Performance Metadata Integrity Protection in the WAFL Copy-on-Write File System. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/kumar) 

##### Abstract 
- We introduce a low-cost incremental checksum technique that protects metadata blocks against in-memory scribbles, and a lightweight digest-based transaction auditing mechanism that enforces file system consistency invariants. Compared with previous work, our techniques reduce performance overhead by an order of magnitude. They also help distinguish scribbles from logic bugs. We also present a mechanism to pinpoint the cause of scribbles on production systems. Our techniques have been productized in the NetApp® WAFL® (Write Anywhere File Layout) file system with negligible performance overhead, greatly reducing corruption-related incidents over the past five years, based on millions of runtime hours. 

### Frameworks 

#### 1. Mirador: An Active Control Plane for Datacenter Storage. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/wires) 

##### Abstract 
- This paper describes  

#### 2. Chronix: Long Term Storage and Retrieval Technology for Anomaly Detection in Operational Data. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/lautenschlager) 

##### Abstract 
- Anomalies in the runtime behavior of software systems, especially in distributed systems, are inevitable, expensive, and hard to locate. To detect and correct such anomalies (like instability due to a growing memory consumption, failure due to load spikes, etc.) one has to automatically collect, store, and analyze the operational data of the runtime behavior, often represented as time series. There are efficient means both to collect and analyze the runtime behavior. But traditional time series databases do not yet focus on the specific needs of anomaly detection (generic data model, specific built-in functions, storage efficiency, and fast query execution). 

- The paper presents Chronix, a domain specific time series database targeted at anomaly detection in operational data. Chronix uses an ideal compression and chunking of the time series data, a methodology for commissioning Chronix’ parameters to a sweet spot, a way of enhancing the data with attributes, an expandable set of analysis functions, and other techniques to achieve both faster query times and a significantly smaller memory footprint. On benchmarks Chronix saves 20%–68% of the space that other time series databases need to store the data and saves 80%–92% of the data retrieval time and 73%–97% of the runtime of analyzing functions. 

#### 3. Crystal: Software-Defined Storage for Multi-Tenant Object Stores. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/gracia-tinedo) 

##### Abstract 
- Object stores are becoming pervasive due to their scalability and simplicity. Their broad adoption, however, contrasts with their rigidity for handling heterogeneous workloads and applications with evolving requirements, which prevents the adaptation of the system to such varied needs. In this work, we present  

### Solid State Records 

#### 1. WORT: Write Optimal Radix Tree for Persistent Memory Storage Systems. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/lee-se-kwon) 

##### Abstract 
- Recent interest in persistent memory (PM) has stirred development of index structures that are efficient in PM. Recent such developments have all focused on variations of the B-tree. In this paper, we show that the radix tree, which is another less popular indexing structure, can be more appropriate as an efficient PM indexing structure. This is because the radix tree structure is determined by the prefix of the inserted keys and also does not require tree rebalancing operations and node granularity updates. However, the radix tree as-is cannot be used in PM. As another contribution, we present three radix tree variants, namely, WORT (Write Optimal Radix Tree), WOART (Write Optimal Adaptive Radix Tree), and ART+CoW. Of these, the first two are optimal for PM in the sense that they only use one 8-byte failure-atomic write per update to guarantee the consistency of the structure and do not require any duplicate copies for logging or CoW. Extensive performance studies show that our proposed radix tree variants perform considerable better than recently proposed B-tree variants for PM such NVTree, wB+Tree, and FPTree for synthetic workloads as well as in implementations within Memcached. 

#### 2. SHRD: Improving Spatial Locality in Flash Storage Accesses by Sequentializing in Host and Randomizing in Device. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/kim) 

##### Abstract 
- Recent advances in flash memory technology have reduced the cost-per-bit of flash storage devices such as solid-state drives (SSDs), thereby enabling the development of large-capacity SSDs for enterprise-scale storage. However, two major concerns arise in designing SSDs. The first concern is the poor performance of random writes in an SSD. Server workloads such as databases generate many random writes; therefore, this problem must be resolved to enable the usage of SSDs in enterprise systems. The second concern is that the size of the internal DRAM of an SSD is proportional to the capacity of the SSD. The peculiarities of flash memory require an address translation layer called flash translation layer (FTL) to be implemented within an SSD. The FTL must maintain the address mapping table in the internal DRAM. Although the previously proposed demand map loading technique can reduce the required DRAM size, the technique aggravates the poor random performance. We propose a novel address reshaping technique called sequentializing in host and randomizing in device (SHRD), which transforms random write requests into sequential write requests in the block device driver by assigning the address space of the reserved log area in the SSD. Unlike previous approaches, SHRD can restore the sequentially written data to the original location without requiring explicit copy operations by utilizing the address mapping scheme of the FTL.We implement SHRD in a real SSD device and demonstrate the improved performance resulting from SHRD for various workloads. 

#### 3. Graphene: Fine-Grained IO Management for Graph Computing. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/liu) 

##### Abstract 
- As graphs continue to grow, external memory graph processing systems serve as a promising alternative to inmemory solutions for low cost and high scalability. Unfortunately, not only does this approach require considerable efforts in programming and IO management, but its performance also lags behind, in some cases by an order of magnitude. In this work, we strive to achieve an ambitious goal of achieving ease of programming and high IO performance (as in-memory processing) while maintaining graph data on disks (as external memory processing). To this end, we have designed and developed  

### Faster Faster 

#### 1. vNFS: Maximizing NFS Performance with Compounds and Vectorized I/O. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/chen) 

##### Abstract 
- Modern systems use networks extensively, accessing both services and storage across local and remote networks. Latency is a key performance challenge, and packing multiple small operations into fewer large ones is an effective way to amortize that cost, especially after years of significant improvement in bandwidth but not latency. To this end, the NFSv4 protocol supports a  

- We propose  

#### 2. On the Accuracy and Scalability of Intensive I/O Workload Replay. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/haghdoost) 

##### Abstract 
- We introduce a replay tool that can be used to replay captured I/O workloads for performance evaluation of high-performance storage systems. We study several sources in the stock operating system that introduce the uncertainty of replaying a workload. Based on the remedies of these findings, we design and develop a new replay tool called  

#### 3. On the Performance Variation in Modern Storage Stacks. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/cao) 

##### Abstract 
- Ensuring stable performance for storage stacks is important, especially with the growth in popularity of hosted services where customers expect QoS guarantees. The same requirement arises from benchmarking settings as well. One would expect that repeated, carefully controlled experiments might yield nearly identical performance results—but we found otherwise. We therefore undertook a study to characterize the amount of variability in benchmarking modern storage stacks. In this paper we report on the techniques used and the results of this study. We conducted many experiments using several popular workloads, file systems, and storage devices—and varied many parameters across the entire storage stack. In over 25% of the sampled configurations, we uncovered variations higher than 10% in storage performance between runs. We analyzed these variations and found that there was no single root cause: it often changed with the workload, hardware, or software configuration in the storage stack. In several of those cases we were able to fix the cause of variation and reduce it to acceptable levels. We believe our observations in benchmarking will also shed some light on addressing stability issues in production systems. 

#### 4. Enlightening the I/O Path: A Holistic Approach for Application Performance. 
- [Source](https://www.usenix.org/conference/fast17/technical-sessions/presentation/kim-sangwook) 

##### Abstract 
- In data-intensive applications, such as databases and keyvalue stores, reducing the request handling latency is important for providing better data services. In such applications, I/O-intensive background tasks, such as checkpointing, are the major culprit in worsening the latency due to the contention in shared I/O stack and storage. To minimize the contention, properly prioritizing I/Os is crucial but the effectiveness of existing approaches is limited for two reasons. First, statically deciding the priority of an I/O is insufficient since high-priority tasks can wait for low-priority I/Os due to  

- In this paper, we propose a  

