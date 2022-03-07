#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.job import MRJob
import sys 

class MRWordCount(MRJob):
    def mapper(self, _, line):
        for word in line.split():
                yield(word, 1)
    def reducer(self, word, counts):
        yield(word, sum(counts))

if __name__ == '__main__':
    MRWordCount.run()