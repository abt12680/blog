# Managed Heap＆CSharp GC Principle(下篇)

本文主要是对《CLR via C#》一书中GC的总结，分上下两篇.  
上篇主要是对GC进行宏观上的概括,下篇主要针对GC的一些细节进行研究

## 目录
- [LargeObjectHeap](#LargeObjectHeap)
- [GCAndPerformance](#GCAndPerformance)
- [InducedCollections](#InducedCollections)
- [延迟模式](#延迟模式)
- [应用程序资源监视](#应用程序资源监视)
- [若引用](#弱引用)

## LargeObjectHeap
CLR 根据将对象分为大对象和小对象,上面所述的Managed Heap其实都是小对象堆，而大对象，在进程地址空间的其他地方进行分配，通常称之为LOH.  
当前,认为大于8500字节的即为大对象,大对象有如下特征:
- 大对象不在Managed Heap 进行分配,在进程地址空间的其他地方分配
- 目前版本的GC不会去压缩大对象,因为在内存中移动他们的代价过高.但这可能在进程中的大对象之间造成地址空间的碎片化,以至于抛出OutOfMemoryException异常.
- 大对象总是在第2代,绝不可能是第0代或第1代，所以只能为需要长时间存活的资源创建大对象.短时间存活的大对象会导致第二代被频繁回收,损害性能.
从.NET Framework 4.5.1开始，可以使用GCSettings.LargeObjectHeapCompactionMode属性按需压缩大对象堆

## GCAndPerformance

.NET 的GC有两种模式,在程序启动时便由CLR指定:  
- __工作站:__ 该模式针对客户端应用程序优化GC.特点是GC造成的延时很低,应用程序线程挂起时间很短,避免使用户感到焦虑,GC假定机器上运行的其他应用程序都不会消耗太多CPU资源.

- __服务器:__ 该模式针对服务端应用程序优化GC.被优化的主要是吞吐量和资源利用.GC假定机器上没有运行其他应用程序

## InducedCollections

## 延迟模式

## 应用程序资源监视

## 弱引用

