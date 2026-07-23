class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        self.following[userId].add(userId)
        for following in self.following[userId]:
            if following in self.tweets:
                index = len(self.tweets[following])-1
                count, tweetId = self.tweets[following][index]
                maxHeap.append([count, tweetId, following, index-1])
        heapq.heapify(maxHeap)
        while len(res) < 10 and maxHeap:
            count, tweetId, following, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[following][index]
                heapq.heappush(maxHeap, [count, tweetId, following, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].discard(followeeId)