class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.tweets.get(userId):
            self.tweets[userId] = []
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        heapq.heapify_max(maxHeap)

        userList = list(self.follows.get(userId)) if self.follows.get(userId) else []
        if userId not in userList:
            userList.append(userId)

        for user in userList:
            if not self.tweets.get(user):
                continue
            for tweet in self.tweets[user]:
                heapq.heappush_max(maxHeap, tweet)

        most_recent = []
        while maxHeap:
            popped = heapq.heappop_max(maxHeap)
            most_recent.append(popped[1])
            if len(most_recent) == 10:
                break
        
        return most_recent

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.follows.get(followerId):
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.follows.get(followerId):
            self.follows[followerId].remove(followeeId)
 