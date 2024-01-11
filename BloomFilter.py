import hashlib

class BloomFilterDeploy:
    def __init__(self):
        pass

    def insertHashes(self,bloomFilter,k,edgeNode1,edgeNode2,nodeID,packetNo):
        m = len(bloomFilter)
        for i in range(k):
            v = int(hashlib.sha256((str(nodeID)+str(edgeNode1)+str(edgeNode2)+str(packetNo)+str(i)).encode()).hexdigest(),16)%m
            bloomFilter[v] = 1
        
    def decodeBloomFilterEdges(self,bloomFilter,nodeIDs,pseudoNodeIDs,packetNo,k):
        fullID = []
        for node in nodeIDs:
            for edge1 in pseudoNodeIDs:
                for edge2 in pseudoNodeIDs:
                    if (edge1 == edge2):
                        continue
                    hashes = []
                    m = len(bloomFilter)
                    verify = False
                    for i in range(k):
                        v = int(hashlib.sha256((str(node)+str(edge1)+str(edge2)+str(packetNo)+str(i)).encode()).hexdigest(),16)%m
                        if bloomFilter[v] != 1:
                            verify = True
                            break
                    if not verify:
                        fullID.append((node,edge1,edge2))

        return fullID
                        # hashes.append(v)

    def constructGraph(self,edges):
        pass
                    
