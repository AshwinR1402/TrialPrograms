def count_substring(string, sub_string):
    a=len(string)
    b=len(sub_string)
    c=a-b+1 
  """c is the number of times that the mainstring can be grouped into 'b' times... ie. "HAPPY","AP" are respected main and subsring,
    "HAPPY" can be seperated into 4 substrings "HA","AP","PP","PY" and now check "AP" is there are not. len("HAPPY")=5 and len("AP")=2.
    so the string is linearly seperated into a-b+1 ie.5-2+1=4  combination"""
    e=0 #here e is the count of substring present in main string
    for i in range(c):
        d=string[i:b]
        b+=1
        if d==sub_string:
           e+=1 
    return e
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
  
  """The built-in function count() cannot give expected output if the substring is overlapped.
  For eg. If a='inini"
  here there are 2 "ini" but count() takes count as 1 and ignores first occurence.now remaining is "ni".
  so count() returns 1.So when the substrings are overlapped in the main string,count() does give wrong answer."""
