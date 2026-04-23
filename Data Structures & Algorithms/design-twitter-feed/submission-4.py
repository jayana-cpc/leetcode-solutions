class Twitter:

    def __init__(self):
        self.followingMap = defaultdict(set)
        self.timeline = []
        heapq.heapify(self.timeline)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        heapq.heappush(self.timeline, (-self.timestamp, tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        res = []
        valid = self.followingMap[userId]
        valid.add(userId)
        i = 0
        size = len(self.timeline)
        while i < size and len(res) < 10:
            tweet = heapq.heappop(self.timeline)
            if tweet[2] in valid:
                res.append(tweet[1])
            tweets.append(tweet)
            i += 1
        for tweet in tweets:
            heapq.heappush(self.timeline, tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].discard(followeeId)

        
          