class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

          district_map = {}
          for i in strs:
             sortwords = sorted(i)
             res = " ".join(sortwords)
             if res not in district_map:
                 district_map[res] = []
             district_map[res].append(i) 
          results = sorted(district_map.values(),key=len)
          return results