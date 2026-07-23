class Twitter:
    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        heapq.heapify(maxHeap)
        if userId not in self.following:
            self.following[userId] = set()
        self.following[userId].add(userId)
        for following in self.following[userId]:
            if following in self.tweets:
                ind = len(self.tweets[following])-1
                cnt, tweetId = self.tweets[following][ind]
                heapq.heappush(maxHeap, [cnt, tweetId, following, ind-1])
        res = []
        while len(res) < 10 and maxHeap:
            cnt, tweetId, following, ind = heapq.heappop(maxHeap)
            res.append(tweetId)
            if ind >= 0:
                cnt, tweetId = self.tweets[following][ind]
                heapq.heappush(maxHeap, [cnt, tweetId, following, ind-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].discard(followeeId)