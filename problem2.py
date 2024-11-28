from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
import re

class SharedPrefixLengthJob(MRJob):
    OUTPUT_PROTOCOL = RawValueProtocol

    def mapper(self, _, line):
        words = re.findall(r'\b[a-z]+\b', line.lower())
        for i in range(1, len(words)):
            yield None, (len(words[i - 1]), len(words[i]), self.shared_prefix(words[i - 1], words[i]))

    def shared_prefix(self, word1, word2):
        prefix_length = 0
        min_length = min(len(word1), len(word2))
        while prefix_length < min_length and word1[prefix_length] == word2[prefix_length]:
            prefix_length += 1
        return prefix_length

    def reducer(self, _, values):
        total_shared_prefix_length = 0
        total_unique_words = 0
        total_word_length = 0

        for length1, length2, prefix_length in values:
            total_shared_prefix_length += prefix_length
            total_unique_words += 1
            total_word_length += length2

        if total_unique_words > 0:
            avg_prefix_length = total_shared_prefix_length / total_unique_words
            avg_word_length = total_word_length / total_unique_words
            result = f"Average Prefix Length: {avg_prefix_length}, Total Unique Words: {total_unique_words}, Average Word Length: {avg_word_length}"
            yield None, result

if __name__ == '__main__':
    SharedPrefixLengthJob.run()
