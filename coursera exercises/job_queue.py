# python3

import heapq

class Worker:
    def __init__(self, thread_id, next_free_time=0):
        self.thread_id = thread_id
        self.next_free_time = next_free_time

    def __lt__(self, other):
        if self.next_free_time == other.next_free_time:
            return self.thread_id < other.thread_id
        return self.next_free_time < other.next_free_time

    def __gt__(self, other):
        if self.next_free_time == other.next_free_time:
            return self.thread_id > other.thread_id
        return self.next_free_time > other.next_free_time

    def __repr__(self):
        return '%s' % self.thread_id

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def assign_jobs_ykp(self):
        # faster algorithm
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        worker_queue = [Worker(i) for i in range(self.num_workers)]
        # next_free_time = [0] * self.num_workers
        # temp = next_free_time[:]
        # heapq.heapify(temp)
        for i in range(len(self.jobs)):
            next_worker = heapq.heappop(worker_queue)
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_worker.next_free_time
            next_worker.next_free_time += self.jobs[i]
            heapq.heappush(worker_queue,next_worker)
          
    def solve(self):
        self.read_data()
        self.assign_jobs_ykp()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
#ykp = JobQueue()
#ykp.num_workers = 2
#ykp.m = 5
#ykp.jobs = [1,2,3,4,5]
#ykp.assign_jobs_ykp()
#ykp.write_response()