class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.count])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId])-1
                tweetId, count = self.tweets[followeeId][index]
                maxHeap.append([count, followeeId, tweetId, index-1])
        heapq.heapify(maxHeap)
        while maxHeap and len(res)<10:
            count, followeeId, tweetId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index>=0:
                tweetId, count = self.tweets[followeeId][index]
                heapq.heappush(maxHeap, [count, followeeId, tweetId, index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].discard(followeeId)