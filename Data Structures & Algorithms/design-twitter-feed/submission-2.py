class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # {uid: [uid...]}
        self.tweets = defaultdict(list) # {uid: [(time, tid)...]}
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        following.add(userId)
        feed = []
        for id in following:
            feed.extend(self.tweets.get(id, []))
        heapq.heapify(feed)
        res = [heapq.heappop(feed) for _ in range(min(len(feed), 10))]
        for tweet in res:
            heapq.heappush(feed, tweet)
        return [tweet[1] for tweet in res]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
