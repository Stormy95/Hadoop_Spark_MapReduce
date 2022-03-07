#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys 

class MRminCategCityPayment(MRJob):
    def mapper_1(self, _, line):
        splitted_line = line.split("\t")
        yield((splitted_line[2],splitted_line[3],splitted_line[5]), float(splitted_line[4]))

    def reducer_1(self, word, counts):
        yield(word,sum(counts))

    def mapper_2(self, word, counts):
        yield((word[0],word[1]), (word[2],counts))

    def reducer_2(self, word, counts):
        yield(word,min(counts))

    def steps(self):
        return [
            MRStep(mapper=self.mapper_1,
                   reducer=self.reducer_1),
            MRStep(mapper=self.mapper_2,
                   reducer=self.reducer_2)
        ]

if __name__ == '__main__':
    MRminCategCityPayment.run()