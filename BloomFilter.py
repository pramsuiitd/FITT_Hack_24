import hashlib

class BloomFilterDeploy:
    def __init__(self):
        pass

    def insertHashes(self,bloomFilter,k,edgeNode1,edgeNode2,nodeID,packetNo):
        m = len(bloomFilter)
        for i in range(k):
            int(hashlib.sha256((str(nodeID)+str(edgeNode1)+str(edgeNode2)+str(packetNo)+str(i)).encode()).hexdigest(),16)%m