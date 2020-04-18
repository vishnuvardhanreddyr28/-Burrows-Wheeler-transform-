def rotate(pattern,d):
    prefix=pattern[:d]
    suffix=pattern[d:]
    return suffix+prefix
    
    
def generate_suffix_array(bwmatrix):
    suffix_array=[]
    for pattern in bwmatrix:
        pos=pattern.find('$')
        suffix_array.append(pos)
    return suffix_array
        
        

def generate(pattern):
    pattern=pattern+'$'
    bwmatrix=[]
    for j in range(len(pattern)):
        bwmatrix.append(rotate(pattern,j))
    print("bwmatrix")
    print(bwmatrix)
    bwmatrix.sort()
    suffix_array=generate_suffix_array(bwmatrix)
    bwstring=''
    for j in range(len(bwmatrix)):
        bwstring+=bwmatrix[j][-1]
    print('bwmatrix sorted')  
    print(bwmatrix)
    print('string which is actually stored')
    print(bwstring)
    print('suffix array')
    print(suffix_array)
    return bwstring,suffix_array

def find_pos(char,column1,nextchar,suffix_array,checked,bwstring):
    pos=-1
    pos_index=[]
    for j in range(len(column1)):
        if(char==column1[j] and bwstring[j]==nextchar and checked[j]==0):
            pos_index.append(j)
            if(suffix_array[j]>pos):
                pos=j
    return pos,pos_index
            
    

def pattern_match(pattern1,pattern2):
    bwstring,suffix_array=generate(pattern1)
    pattern2=pattern2[::-1]
    column1=list(bwstring)
    column1.sort()
    print("The first column obtained")
    print(column1)
    checked=[]
    pos=-1
    for j in range(len(suffix_array)):
        checked.append(0)
    for j in range(len(pattern2)-1):
        pos,pos_index=find_pos(pattern2[j],column1,pattern2[j+1],suffix_array,checked,bwstring)
        if(pos==-1):
            print("no match of pattern found")
            break
        else:
            checked[pos]=1
    if(pos!=-1):
        print('pattern occurs at the following index')
        for pos in pos_index:
            print(len(pattern1)-suffix_array[pos]-1)
   
    
pattern_match("panamabanana","ana")