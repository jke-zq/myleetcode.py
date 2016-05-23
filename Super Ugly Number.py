import heapq
class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        # maxheap = []
        # heapq.heappush(maxheap, 1)
        # n -= 1
        # sets = set(maxheap)
        # while n:
        #     val = heapq.heappop(maxheap)
        #     n -= 1
        #     for f in primes:
        #         ## error: val = f * val
        #         nval = f * val
        #         if nval not in sets:
        #             heapq.heappush(maxheap, nval)
        #             sets.add(nval)
        # return maxheap[0]

        ## cant understand this solution
        # heap, uglies, idx, ugly_by_last_prime = [], [0] * n, [0] * len(primes), [0] * n
        # uglies[0] = 1

        # for k, p in enumerate(primes):
        #     heapq.heappush(heap, (p, k))

        # for i in xrange(1, n):
        #     uglies[i], k = heapq.heappop(heap)
        #     ugly_by_last_prime[i] = k
        #     idx[k] += 1
        #     while ugly_by_last_prime[idx[k]] > k:
        #         idx[k] += 1
        #     heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

        # return uglies[-1]

        ## easy to understand
        length = len(primes)
        times = [0] * length
        uglys = [1]
        minlist = [(primes[i] * uglys[times[i]], i) for i in xrange(len(times))]
        heapq.heapify(minlist)

        while len(uglys) < n:
            (umin, min_times) = heapq.heappop(minlist)
            times[min_times] += 1
            if umin != uglys[-1]:
                uglys.append(umin)
            heapq.heappush(minlist, (primes[min_times] * uglys[times[min_times]], min_times))

        return uglys[-1] 
if __name__ == '__main__':
    print Solution().nthSuperUglyNumber(6, [5, 3])