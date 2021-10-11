def col_swap(x,i,j): # Swap the columns of Adjancy matrix of graph
    temp =copy(x[:,i])
    x[:,i] = x[:,j]
    x[:,j] = temp
    return x
def row_swap(x,i,j): # Swap the rows of Adjancy matrix of graph
    temp =copy(x[i,:])
    x[i,:] = x[j,:]
    x[j,:] = temp
    return x
# Take input as arrays and reshape to adjancy matrix for graph
# with nodes and edges
def Config_Check(A): 
    A= reshape(A,(9,9))
    print("-------------------")
    print (A)
    G = Graph()
    G = from_numpy_matrix(A)
    Edges = G.edges()
    Nodes = G.nodes()
    print('Nodes :',Nodes)
    N_E = G.number_of_edges()
    print('Number of edges :',N_E)
    print('Edges :',Edges)
    
def Config_Check(A):
    A= reshape(A,(9,9))
    print "-------------------"
    print A
    G = Graph()
    G = from_numpy_matrix(A)
    Edges = G.edges()
    Nodes = G.nodes()
    print('Nodes :',Nodes)
    N_E = G.number_of_edges()
    print('Number of edges :',N_E)
    print('Edges :',Edges)
    R1_s12 = A[0][6]+A[0][7]
    R2_s12 = A[1][6]+A[1][7]
    C1_s12 = A[3][6]+A[3][7]
    C2_s12 = A[4][6]+A[4][7]
    Con_fig_M2b2_s12 = reshape([A[0][3:5],A[1][3:5]],(2,2))
    #print Con_fig_M2b2_s12
    E_K3K1_s12 = [[R1_s12],[R2_s12]]
    Con_fig_M3b2_s12 = concatenate((E_K3K1_s12,Con_fig_M2b2_s12), axis = 1)
    #print Con_fig_M3b2_s12
    E_K3K2_s12 = [[0,C1_s12,C2_s12]]
    S12 = concatenate((E_K3K2_s12,Con_fig_M3b2_s12), axis = 0)
    print("Subgraph Color Class 1 & 2")
    print S12
    print(" ")
    print S12[1:3,0:3]
    sum_r12 = sum(S12[1:3,0:3])
    print('RowS12um    =  ',sum_r12)
    print S12[0:3,1:3]
    sum_c12 = sum(S12[0:3,1:3])
    print('ColumnS12um =  ',sum_c12)
    Top_Row12 = sum(S12[0:1,0:3])
    print("Top Row")
    print(S12[0:1,0:3])
    print('Top_Row12   = ' ,Top_Row12)
    Left_Col12 = sum(S12[0:3,0:1])
    print("Lef Column")
    print(S12[0:3,0:1])
    print('Left_Col12  = ' ,Left_Col12)
    print("-------------------")
    print(Left_Col12,sum_r12,sum_c12,Top_Row12)
    print("-------------------")
    
#------------ Graph 1 and 2-------Start

    ME_12=0
    M03_12=0
    M14_12=0
    M36_12=0
    M47_12=0
    M06_12=0
    M17_12=0
    # Case-1 (EEEE) or (OEEO)
    if(Left_Col12%2==0 and sum_r12%2==0 and sum_c12%2==0 and Top_Row12%2==0)or(Left_Col12%2!=0 and sum_r12%2==0 and sum_c12%2==0 and Top_Row12%2!=0): 
        ME_s12 = 1
    # Case-2 (OOOO) or (EOOE)
    if(Left_Col12%2!=0 and sum_r12%2!=0 and sum_c12%2!=0 and Top_Row12%2!=0)or(Left_Col12%2==0 and sum_r12%2!=0 and sum_c12%2!=0 and Top_Row12%2==0):
        if (A[0][3]==1 and A[1][4]==0):
           if ((sum_r12-A[0][3])%2==0 and (sum_c12-A[0][3])%2==0):
               sum_r12 = sum_r12-A[0][3]
               sum_c12=sum_c12-A[0][3]
               M03_12=1
        if (A[0][3]==0 and A[1][4]==1):
            if ((sum_r12-A[1][4])%2==0 and (sum_c12-A[1][4])%2==0):
                sum_r12 = sum_r12-A[1][4]
                sum_c12=sum_c12-A[1][4]
                M14_12=1
        if (A[0][3]==1 and A[1][4]==1):
            if ((sum_r12-A[0][3])%2==0 and (sum_c12-A[0][3])%2==0):
                sum_r12 = sum_r12-A[0][3]
                sum_c12=sum_c12-A[0][3]
                M03_12=1
    #Case-3 (EEOO) or (OEOE)
    if(Left_Col12%2==0 and sum_r12%2==0 and sum_c12%2!=0 and Top_Row12%2!=0)or(Left_Col12%2!=0 and sum_r12%2==0 and sum_c12%2!=0 and Top_Row12%2==0):
        if (A[3][6]==1 and A[4][7]== 0):
            if ((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2==0):
                sum_c12 = sum_c12-A[3][6]
                Top_Row12 = Top_Row12-A[3][6]
                M36_12=1
        if (A[3][6]==0 and A[4][7]== 1):
            if ((sum_c12-A[4][7])%2==0 and (Top_Row12-A[4][7])%2==0):
                sum_c12 = sum_c12-A[4][7]
                Top_Row12 = Top_Row12-A[4][7]
                M47_12=1
        if (A[3][6]==1 and A[4][7]== 1):
            if ((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2==0):
                sum_c12 = sum_c12-A[3][6]
                Top_Row12 = Top_Row12-A[3][6]
                M36_12=1
        if (A[3][6]==1 and A[4][7]== 0):
            if ((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2!=0):
                sum_c12 = sum_c12-A[3][6]
                Top_Row12 = Top_Row12-A[3][6]
                M36_12=1
        if (A[3][6]==0 and A[4][7]== 1):
            if ((sum_c12-A[4][7])%2==0 and (Top_Row12-A[4][7])%2!=0):
                sum_c12 = sum_c12-A[4][7]
                Top_Row12 = Top_Row12-A[4][7]
                M47_12=1
        if (A[3][6]==1 and A[4][7]== 1):
            if ((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2!=0):
                sum_c12 = sum_c12-A[3][6]
                Top_Row12 = Top_Row12-A[3][6]
                M36_12=1
        #-------------------------------
        if ((A[0][6]==1 and A[0][3]==1) and (A[1][7]==0 and A[1][4]==0)) or ((A[0][6]==1 and A[0][3]==1) and (A[1][7]==1 and A[1][4]==1)):    
            if ((Left_Col12-A[0][6])%2==0 and (sum_r12-A[0][6]-A[0][3])%2==0) and((sum_c12-A[0][3])%2==0 and (Top_Row12)%2==0):
                Left_Col12 = Left_Col12-A[0][6]
                sum_r12 = sum_r12-A[0][6]-A[0][3]
                M06_12=1
                sum_c12 = sum_c12-A[0][3]
                M03_12=1
        if (A[0][6]==1 and A[0][3]==0) and (A[1][7]==0 and A[1][4]==1):    
            if ((Left_Col12-A[0][6])%2==0 and (sum_r12-A[0][6]-A[1][4])%2==0) and((sum_c12-A[1][4])%2==0 and (Top_Row12)%2==0):
                Left_Col12 = Left_Col12-A[0][6]
                sum_r12 = sum_r12-A[0][6]-A[1][4]
                M06_12=1
                sum_c12 = sum_c12-A[1][4]
                M14_12=1
        if (A[0][6]==0 and A[0][3]==1) and (A[1][7]==1 and A[1][4]==0):    
            if ((Left_Col12-A[1][7])%2==0 and (sum_r12-A[1][7]-A[0][3])%2==0) and((sum_c12-A[0][3])%2==0 and (Top_Row12)%2==0):
                Left_Col12 = Left_Col12-A[1][7]
                sum_r12 = sum_r12-A[1][7]-A[0][3]
                M17_12=1
                sum_c12 = sum_c12-A[0][3]
                M03_12=1
        if (A[0][6]==0 and A[0][3]==0) and (A[1][7]==1 and A[1][4]==1):    
            if ((Left_Col12-A[1][7])%2==0 and (sum_r12-A[1][7]-A[1][4])%2==0) and((sum_c12-A[1][4])%2==0 and (Top_Row12)%2!=0):
                Left_Col12 = Left_Col12-A[1][7]
                sum_r12 = sum_r12-A[1][7]-A[1][4]
                M17_12=1
                sum_c12 = sum_c12-A[1][7]
                M14_12=1
        #--------------------------------
    #Case-4 (OOEE) or (EOEO)
    if (Left_Col12%2!=0 and sum_r12%2!=0 and sum_c12%2==0 and Top_Row12%2==0)or(Left_Col12%2==0 and sum_r12%2!=0 and sum_c12%2==0 and Top_Row12%2!=0): 
        if (A[0][6]==1 and A[1][7]==0 ):
            if ((Left_Col12-A[0][6])%2==0 and (sum_r12-A[0][6])%2==0):
                Left_Col12 = Left_Col12-A[0][6]
                sum_r12 = sum_r12-A[0][6]
                M06_12=1
        if (A[0][6]==0 and A[1][7]==1 ):
            if ((Left_Col12-A[1][7])%2==0 and (sum_r12-A[1][7])%2==0):
                Left_Col12 = Left_Col12-A[1][7]
                sum_r12 = sum_r12-A[1][7]
                M17_12=1
        if (A[0][6]==1 and A[1][7]==1 ):
            if ((Left_Col12-A[0][6])%2==0 and (sum_r12-A[0][6])%2==0):
                Left_Col12 = Left_Col12-A[0][6]
                sum_r12 = sum_r12-A[0][6]
                M06_12=1
        if (A[0][6]==1 and A[1][7]==0 ):
            if ((Left_Col12-A[0][6])%2!=0 and (sum_r12-A[0][6])%2==0):
                Left_Col12 = Left_Col12-A[0][6]
                sum_r12 = sum_r12-A[0][6]
                M06_12=1
        if (A[0][6]==0 and A[1][7]==1 ):
            if ((Left_Col12-A[1][7])%2!=0 and (sum_r12-A[1][7])%2==0):
                Left_Col12 = Left_Col12-A[1][7]
                sum_r12 = sum_r12-A[1][7]
                M17_12=1
        if (A[0][6]==1 and A[1][7]==1 ):
            if ((Left_Col12-A[0][6])%2!=0 and (sum_r12-A[0][6])%2==0):
                Left_Col12 = Left_Col12-A[0][6]
                sum_r12 = sum_r12-A[0][6]
                M06_12=1
    #Case-5 (OOOO),A[0][3]=0,A[1][4]=0,
    if (A[0][3]==0 and A[1][4]==0):
        if(Left_Col12%2!=0 and sum_r12%2!=0 and sum_c12%2!=0 and Top_Row12%2!=0):
            if ((A[0][6]==1 and A[3][6]==1) and (A[1][7]==0 and A[4][7]==0)) or ((A[0][6]==1 and A[3][6]==1) and (A[1][7]==1 and A[4][7]==1)):    
                if ((Left_Col12-A[0][6])%2==0 and (sum_r12-A[0][6])%2==0) and((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2==0):
                    Left_Col12 = Left_Col12-A[0][6]
                    sum_r12 = sum_r12-A[0][6]
                    M06_12=1
                    sum_c12 = sum_c12-A[3][6]
                    Top_Row12=Top_Row12-A[3][6]
                    M36_12=1
            if (A[0][6]==0 and A[3][6]==0) and (A[1][7]==1 and A[4][7]==1):    
                if ((Left_Col12-A[1][7])%2!=0 and (sum_r12-A[1][7])%2==0) and((sum_c12-A[4][7])%2==0 and (Top_Row12-A[4][7])%2!=0):
                    Left_Col12 = Left_Col12-A[1][7]
                    sum_r12 = sum_r12-A[1][7]
                    M17_12=1
                    sum_c12 = sum_c12-A[4][7]
                    Top_Row12=Top_Row12-A[4][7]
                    M47_12=1
            if (A[0][6]==1 and A[3][6]==0) and (A[1][7]==0 and A[4][7]==1):    
                if ((Left_Col12-A[0][6])%2!=0 and (sum_r12-A[0][6])%2==0) and((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2!=0):
                    Left_Col12 = Left_Col12-A[0][6]
                    sum_r12 = sum_r12-A[0][6]
                    M06_12=1
                    sum_c12 = sum_c12-A[4][7]
                    Top_Row12=Top_Row12-A[4][7]
                    M47_12=1
            if (A[0][6]==0 and A[3][6]==1) and (A[1][7]==1 and A[4][7]==0):    
                if ((Left_Col12-A[3][6])%2!=0 and (sum_r12-A[3][6])%2==0) and((sum_c12-A[1][7])%2==0 and (Top_Row12-A[1][7])%2!=0):
                    Left_Col12 = Left_Col12-A[3][6]
                    sum_r12 = sum_r12-A[3][6]
                    M36_12=1
                    sum_c12 = sum_c12-A[1][7]
                    Top_Row12=Top_Row12-A[1][7]
                    M17_12=1
    #Case-6 (EOOE),A[0][3]=0,A[1][4]=0,
    if (A[0][3]==0 and A[1][4]==0):
        if (Left_Col12%2==0 and sum_r12%2!=0 and sum_c12%2!=0 and Top_Row12%2==0):
            if ((A[0][6]==1 and A[3][6]==1) and (A[1][7]==0 and A[4][7]==0)) or ((A[0][6]==1 and A[3][6]==1) and (A[1][7]==1 and A[4][7]==1)):    
                if ((Left_Col12-A[0][6])%2!=0 and (sum_r12-A[0][6])%2==0) and((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2!=0):
                    Left_Col12 = Left_Col12-A[0][6]
                    sum_r12 = sum_r12-A[0][6]
                    M06_12=1
                    sum_c12 = sum_c12-A[3][6]
                    Top_Row12=Top_Row12-A[3][6]
                    M36_12=1
            if (A[0][6]==0 and A[3][6]==0) and (A[1][7]==1 and A[4][7]==1): 
                if ((Left_Col12-A[1][7])%2!=0 and (sum_r12-A[1][7])%2==0) and((sum_c12-A[4][7])%2==0 and (Top_Row12-A[4][7])%2!=0):
                    Left_Col12 = Left_Col12-A[1][7]
                    sum_r12 = sum_r12-A[1][7]
                    M17_12=1
                    sum_c12 = sum_c12-A[4][7]
                    Top_Row12=Top_Row12-A[4][7]
                    M47_12=1
            if (A[0][6]==1 and A[3][6]==0) and (A[1][7]==0 and A[4][7]==1):    
                if ((Left_Col12-A[0][6])%2!=0 and (sum_r12-A[0][6])%2==0) and((sum_c12-A[3][6])%2==0 and (Top_Row12-A[3][6])%2!=0):
                    Left_Col12 = Left_Col12-A[0][6]
                    sum_r12 = sum_r12-A[0][6]
                    M06_12=1
                    sum_c12 = sum_c12-A[4][7]
                    Top_Row12=Top_Row12-A[4][7]
                    M47_12=1
            if (A[0][6]==0 and A[3][6]==1) and (A[1][7]==1 and A[4][7]==0):    
                if ((Left_Col12-A[3][6])%2!=0 and (sum_r12-A[3][6])%2==0) and((sum_c12-A[1][7])%2==0 and (Top_Row12-A[1][7])%2!=0):
                    Left_Col12 = Left_Col12-A[3][6]
                    sum_r12 = sum_r12-A[3][6]
                    M36_12=1
                    sum_c12 = sum_c12-A[1][7]
                    Top_Row12=Top_Row12-A[1][7]
                    M17_12=1

    #-----------------------------------------------------------------
    #Case-7 (OOEE),A[0][6]=0,A[1][7]=0
        if (A[0][6]==0 and A[1][7]==0):
            if (Left_Col12%2!=0 and sum_r12%2!=0 and sum_c12%2==0 and Top_Row12%2==0):
                if ((A[0][3]==1 and A[3][6]==1) and (A[1][4]==0 and A[4][7]==0))or ((A[0][3]==1 and A[3][6]==1) and (A[1][4]==0 and A[4][7]==0)):
                    if ((sum_r12-A[0][3])%2==0 and (sum_c12-A[0][3]-A[3][6])%2==0 and (Top_Row12-A[3][6])%2!=0):
                        sum_r12 = sum_r12-A[0][3]
                        sum_c12 = sum_c12-A[0][3]-A[3][6]
                        Top_Row12 = Top_Row12-A[3][6]
                        M03_23=1
                        M36_23=1
                if ((A[0][3]==0 and A[3][6]==0) and (A[1][4]==1 and A[4][7]==1)):
                    if ((sum_r12-A[1][4])%2==0 and (sum_c12-A[1][4]-A[4][7])%2==0 and (Top_Row12-A[4][7])%2!=0):
                        sum_r12 = sum_r12-A[1][4]
                        sum_c12 = sum_c12-A[1][4]-A[4][7]
                        Top_Row12 = Top_Row12-A[4][7]
                        M14_23=1
                        M47_23=1
                if ((A[0][3]==1 and A[3][6]==0) and (A[1][4]==0 and A[4][7]==1)):
                    if ((sum_r12-A[0][3])%2==0 and (sum_c12-A[0][3]-A[4][7])%2==0 and (Top_Row12-A[4][7])%2!=0):
                        sum_r12 = sum_r12-A[0][3]
                        sum_c12 = sum_c12-A[0][3]-A[4][7]
                        Top_Row12 = Top_Row12-A[4][7]
                        M03_23=1
                        M47_23=1
                if ((A[0][3]==0 and A[3][6]==1) and (A[1][4]==1 and A[4][7]==0)):
                    if ((sum_r12-A[3][6])%2==0 and (sum_c12-A[3][6]-A[1][4])%2==0 and (Top_Row12-A[1][4])%2!=0):
                        sum_r12 = sum_r12-A[3][6]
                        sum_c12 = sum_c12-A[3][6]-A[1][4]
                        Top_Row12 = Top_Row12-A[1][4]
                        M36_23=1
                        M14_23=1
    #Case-8 (EEOO),A[3][6]=0,A[4][7]=0
        if (A[3][6]==0 and A[4][7]==0):
            if (Left_Col12%2==0 and sum_r12%2==0 and sum_c12%2!=0 and Top_Row12%2!=0):
                if ((A[0][3]==1 and A[0][6]==1) and (A[1][4]==0 and A[1][7]==0))or ((A[0][3]==1 and A[0][6]==1) and (A[1][4]==0 and A[1][7]==0)):
                    if ((Left_Col12-A[0][6])%2and (sum_r12-A[0][3]-A[0][6])%2==0 and (sum_c12-A[0][3])%2==0):
                        sum_r12 = sum_r12-A[0][3]-A[0][6]
                        sum_c12 = sum_c12-A[0][3]
                        Left_Col12 = Left_Col12-A[0][6]
                        M06_23=1
                        M36_23=1
                if ((A[0][3]==0 and A[0][6]==0) and (A[1][4]==1 and A[1][7]==1)):
                    if ((Left_Col12-A[1][7])%2and (sum_r12-A[1][4]-A[1][7])%2==0 and (sum_c12-A[1][4])%2==0):
                        sum_r12 = sum_r12-A[1][4]-A[1][7]
                        sum_c12 = sum_c12-A[1][4]
                        Left_Col12 = Left_Col12-A[1][7]
                        M14_23=1
                        M17_23=1
                if ((A[0][3]==1 and A[0][6]==0) and (A[1][4]==0 and A[1][7]==1)):
                    if ((Left_Col12-A[1][7])%2and (sum_r12-A[0][3]-A[1][7])%2==0 and (sum_c12-A[0][3])%2==0):
                        sum_r12 = sum_r12-A[0][3]-A[1][7]
                        sum_c12 = sum_c12-A[0][3]
                        Left_Col12 = Left_Col12-A[1][7]
                        M03_23=1
                        M17_23=1
                        
                if ((A[0][3]==0 and A[0][6]==1) and (A[1][4]==1 and A[1][7]==0)):
                    if ((Left_Col12-A[0][6])%2and (sum_r12-A[0][6]-A[1][4])%2==0 and (sum_c12-A[1][4])%2==0):
                        sum_r12 = sum_r12-A[0][6]-A[1][4]
                        sum_c12 = sum_c12-A[1][4]
                        Left_Col12 = Left_Col12-A[0][6]
                        M03_23=1
                        M17_23=1
    #Case-9 (EOOO),A[3][6]=0,A[4][7]=0
    #Case-9 (OOOE),A[3][6]=0,A[4][7]=0

    print("-------------------")
    print(Left_Col12,sum_r12,sum_c12,Top_Row12)
    print ("-------------------")
    if (Left_Col12%2==0 and sum_r12%2==0 and sum_c12%2==0 and Top_Row12%2==0) or (Left_Col12%2!=0 and sum_r12%2==0 and sum_c12%2==0 and Top_Row12%2!=0):
        print("CDC exists, good configuration")
        return 2
    else:
        print("CDC does not exist, bad configuration")
        return 3
    #------------ Graph 1 and 2-------End
    
    #print("M47_12=",M47_12)
    #------------ Graph 2 and 3-------Start
    R2_23 = A[1][7]+A[1][8]        
    R3_23 = A[2][7]+A[2][8]
    C2_23 = A[4][7]+A[4][8]
    C3_23 = A[5][7]+A[5][8]
    Con_fig_M2b2_23 = reshape([A[1][4:6],A[2][4:6]],(2,2))
    #print Con_fig_M2b2_23
    E_K3K1_23 = [[R2_23],[R3_23]]
    Con_fig_M3b2_23 = concatenate((E_K3K1_23,Con_fig_M2b2_23), axis = 1)
    #print Con_fig_M3b2_23
    E_K3K2_23 = [[0,C2_23,C3_23]]
    S23 = concatenate((E_K3K2_23,Con_fig_M3b2_23), axis = 0)
    print("Subgraph Color Class 2 & 3")
    print(S23)
    print(" ")
    print S23[1:3,0:3]
    sum_r23 = sum(S23[1:3,0:3])
    print('RowS23um    =  ',sum_r23)
    print(S23[0:3,1:3])
    sum_c23 = sum(S23[0:3,1:3])
    print('ColumnS23um =  ',sum_c23)
    Top_Row23 = sum(S23[0:1,0:3])
    print("Top Row")
    print(S23[0:1,0:3])
    print('Top_Row23   =  ',Top_Row23)
    Left_Col23 = sum(S23[0:3,0:1])
    print("Lef Column")
    print(S23[0:3,0:1])
    print('Left_Col23  =  ',Left_Col23)
    print("-------------------")
    print(Left_Col23,sum_r23,sum_c23,Top_Row23)
    print("-------------------")
    ME_23 =0
    M14_23=0
    M25_23=0
    M47_23=0
    M58_23=0
    M17_23=0
    M28_23=0

    # Here E stands for even number of edges and O for odd.
    # Case-1 (EEEE) or (OEEO)
    if (Left_Col23%2==0 and sum_r23%2==0 and sum_c23%2==0 and Top_Row23%2==0)or(Left_Col23%2!=0 and sum_r23%2==0 and sum_c23%2==0 and Top_Row23%2!=0): 
        ME_23 =1
    # Case-2 (OOOO) or (EOOE)
    if (M14_12==0):
        if (Left_Col23%2!=0 and sum_r23%2!=0 and sum_c23%2!=0 and Top_Row23%2!=0)or(Left_Col23%2==0 and sum_r23%2!=0 and sum_c23%2!=0 and Top_Row23%2==0):
            if (A[1][4]==1 and A[2][5]==0):
                if ((sum_r23-A[1][4])%2==0 and (sum_c23-A[1][4])%2==0):
                    sum_r23 = sum_r23-A[1][4]
                    sum_c23=sum_c23-A[1][4]
                    M14_23=1
            if (A[1][4]==0 and A[2][5]==1):
                if ((sum_r23-A[2][5])%2==0 and (sum_c23-A[2][5])%2==0):
                    sum_r23 = sum_r23-A[2][5]
                    sum_c23=sum_c23-A[2][5]
                    M25_23=1
            if (A[1][4]==1 and A[2][5]==1):
                if ((sum_r23-A[1][4])%2==0 and (sum_c23-A[1][4])%2==0):
                    sum_r23 = sum_r23-A[1][4]
                    sum_c23=sum_c23-A[1][4]
                    M14_23=1
    if (M14_12==1):
        if (Left_Col23%2!=0 and sum_r23%2!=0 and sum_c23%2!=0 and Top_Row23%2!=0)or(Left_Col23%2==0 and sum_r23%2!=0 and sum_c23%2!=0 and Top_Row23%2==0):
            if (A[1][4]==1 and A[2][5]==0):
                if (sum_r23%2==0 and sum_c23%2==0):
                    sum_r23 = sum_r23- 0
                    sum_c23=sum_c23- 0
            if (A[1][4]==0 and A[2][5]==1):
                if ((sum_r23-A[2][5])%2==0 and (sum_c23-A[2][5])%2==0):
                    sum_r23 = sum_r23-A[2][5]
                    sum_c23=sum_c23-A[2][5]
                    M25_23=1
            if (A[1][4]==1 and A[2][5]==1):
                if (sum_r23%2==0 and sum_c23%2==0):
                    sum_r23 = sum_r23- 0
                    sum_c23=sum_c23- 0
    # Case-3 (EEOO) or (OEOE) 
    if (M47_12==0):
        if (Left_Col23%2==0 and sum_r23%2==0 and sum_c23%2!=0 and Top_Row23%2!=0)or(Left_Col23%2!=0 and sum_r23%2==0 and sum_c23%2!=0 and Top_Row23%2==0):
            if (A[4][7]==1 and A[5][8]== 0):
                if ((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2==0):
                    sum_c23 = sum_c23-A[4][7]
                    Top_Row23 = Top_Row23-A[4][7]
                    M47_23=1
            if (A[4][7]==0 and A[5][8]== 1):
                if ((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2==0):
                    sum_c23 = sum_c23-A[5][8]
                    Top_Row23 = Top_Row23-A[5][8]
                    M58_23=1
            if (A[4][7]==1 and A[5][8]== 1):
                if ((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2==0):
                    sum_c23 = sum_c23-A[4][7]
                    Top_Row23 = Top_Row23-A[4][7]
                    M47_23=1
            if (A[4][7]==1 and A[5][8]== 0):
                if ((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2!=0):
                    sum_c23 = sum_c23-A[4][7]
                    Top_Row23 = Top_Row23-A[4][7]
                    M47_23=1
            if (A[4][7]==0 and A[5][8]== 1):
                if ((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2!=0):
                    sum_c23 = sum_c23-A[5][8]
                    Top_Row23 = Top_Row23-A[5][8]
                    M58_23=1
            if (A[4][7]==1 and A[5][8]== 1):
                if ((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2!=0):
                    sum_c23 = sum_c23-A[4][7]
                    Top_Row23 = Top_Row23-A[4][7]
                    M47_23=1
    if (M47_12==1):
        if (Left_Col23%2==0 and sum_r23%2==0 and sum_c23%2!=0 and Top_Row23%2!=0)or(Left_Col23%2!=0 and sum_r23%2==0 and sum_c23%2!=0 and Top_Row23%2==0):
            if (A[4][7]==1 and A[5][8]== 0):
                if (sum_c23%2==0 and Top_Row23%2==0):
                    sum_c23 = sum_c23- 0
                    Top_Row23 = Top_Row23- 0
            if (A[4][7]==0 and A[5][8]== 1):
                if ((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2==0):
                    sum_c23 = sum_c23-A[5][8]
                    Top_Row23 = Top_Row23-A[5][8]
                    M58_23=1
            if (A[4][7]==1 and A[5][8]== 1):
                if (sum_c23%2==0 and Top_Row23%2==0):
                    sum_c23 = sum_c23- 0
                    Top_Row23 = Top_Row23- 0
            if (A[4][7]==1 and S23[0][2]== 0):
                if (sum_c23%2==0 and Top_Row23%2!=0):
                    sum_c23 = sum_c23- 0
                    Top_Row23 = Top_Row23- 0
            if (A[4][7]==0 and A[5][8]== 1):
                if ((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2!=0):
                    sum_c23 = sum_c23-A[5][8]
                    Top_Row23 = Top_Row23-A[5][8]
                    M58_23=1
            if (A[4][7]==1 and A[5][8]== 1):
                if (sum_c23%2==0 and Top_Row23%2!=0):
                    sum_c23 = sum_c23- 0
                    Top_Row23 = Top_Row23- 0

    # Case-4 (OOEE) or (EOEO)
    if (M17_12==0 or M14_12==0 or M47_12==0):
        if (Left_Col23%2!=0 and sum_r23%2!=0 and sum_c23%2==0 and Top_Row23%2==0)or(Left_Col23%2==0 and sum_r23%2!=0 and sum_c23%2==0 and Top_Row23%2!=0):
            if (A[1][7]==1 and A[2][8]==0 ):
                if ((Left_Col23-A[1][7])%2==0 and (sum_r23-A[1][7])%2==0):
                    Left_Col23 = Left_Col23-A[1][7]
                    sum_r23 = sum_r23-A[1][7]
                    M17_23=1   
            if (A[1][7]==0 and A[2][8]==1 ):
                if ((Left_Col23-A[2][8])%2==0 and (sum_r23-A[2][8])%2==0):
                    Left_Col23 = Left_Col23-A[2][8]
                    sum_r23 = sum_r23-A[2][8]
                    M28_23=1
            if (A[1][7]==1 and A[2][8]==1 ):
                if ((Left_Col23-A[1][7])%2==0 and (sum_r23-A[1][7])%2==0):
                    Left_Col23 = Left_Col23-A[1][7]
                    sum_r23 = sum_r23-A[1][7]
                    M17_23=1
            if (A[1][7]==1 and A[2][8]==0 ):
                if ((Left_Col23-A[1][7])%2!=0 and (sum_r23-A[1][7])%2==0):
                    Left_Col23 = Left_Col23-A[1][7]
                    sum_r23 = sum_r23-A[1][7]
                    M17_23=1   
            if (A[1][7]==0 and A[2][8]==1 ):
                if ((Left_Col23-A[2][8])%2!=0 and (sum_r23-A[2][8])%2==0):
                    Left_Col23 = Left_Col23-A[2][8]
                    sum_r23 = sum_r23-A[2][8]
                    M28_23=1
            if (A[1][7]==1 and A[2][8]==1 ):
                if ((Left_Col23-A[1][7])%2==0 and (sum_r23-A[1][7])%2==0):
                    Left_Col23 = Left_Col23-A[1][7]
                    sum_r23 = sum_r23-A[1][7]
                    M17_23=1
            if ((A[1][4]==1 and A[4][7]==1) and(A[2][5]==0 and A[5][8]==0)) or ((A[1][4]==1 and A[4][7]==1) and(A[2][5]==1 and A[5][8]==1)):
                if (Left_Col23%2==0 and (sum_r23-A[1][4])%2==0 and (sum_c23-A[1][4]-A[4][7])%2==0 and (Top_Row23-A[4][7])%2==0):
                    sum_r23=sum_r23-A[1][4]
                    sum_c23=sum_c23-A[1][4]-A[4][7]
                    Top_Row23=Top_Row23-A[4][7]
                    M14_23=0
                    M47_23=0
            if ((A[1][4]==1 and A[4][7]==0) and(A[2][5]==0 and A[5][8]==1)):
                if (Left_Col23%2==0 and (sum_r23-A[1][4])%2==0 and (sum_c23-A[1][4]-A[5][8])%2==0 and (Top_Row23-A[5][8])%2==0):
                    sum_r23=sum_r23-A[1][4]
                    sum_c23=sum_c23-A[1][4]-A[5][8]
                    Top_Row23=Top_Row23-A[5][8]
                    M14_23=0
                    M58_23=0
            if ((A[1][4]==0 and A[4][7]==1) and(A[2][5]==1 and A[5][8]==0)):
                if (Left_Col23%2==0 and (sum_r23-A[2][5])%2==0 and (sum_c23-A[2][5]-A[4][7])%2==0 and (Top_Row23-A[4][7])%2==0):
                    sum_r23=sum_r23-A[2][5]
                    sum_c23=sum_c23-A[2][5]-A[4][7]
                    Top_Row23=Top_Row23-A[4][7]
                    M25_23=0
                    M47_23=0
            if ((A[1][4]==0 and A[4][7]==0) and(A[2][5]==1 and A[5][8]==1)):
                if (Left_Col23%2==0 and (sum_r23-A[2][5])%2==0 and (sum_c23-A[2][5]-A[5][8])%2==0 and (Top_Row23-A[5][8])%2==0):
                    sum_r23=sum_r23-A[2][5]
                    sum_c23=sum_c23-A[2][5]-A[5][8]
                    Top_Row23=Top_Row23-A[5][8]
                    M25_23=0
                    M58_23=0
    if (M17_12==1):
        if (Left_Col23%2!=0 and sum_r23%2!=0 and sum_c23%2==0 and Top_Row23%2==0)or(Left_Col23%2==0 and sum_r23%2!=0 and sum_c23%2==0 and Top_Row23%2!=0):
            if (A[1][7]==1 and A[2][8]==0 ):
                if (Left_Col23%2==0 and sum_r23%2==0):
                    Left_Col23 = Left_Col23- 0
                    sum_r23 = sum_r23- 0 
            if (A[1][7]==0 and S23[2][0]==1 ):
                if ((Left_Col23-A[2][8])%2==0 and (sum_r23-A[2][8])%2==0):
                    Left_Col23 = Left_Col23-A[2][8]
                    sum_r23 = sum_r23-A[2][8]
                    M28_23=1
            if (A[1][7]==1 and A[2][8]==1 ):
                if (Left_Col23%2==0 and sum_r23%2==0):
                    Left_Col23 = Left_Col23- 0
                    sum_r23 = sum_r23- 0

     #Case-5 (EOOE),A[1][4]=0,A[2][5]=0
     # M17_12=0,M47_12=0
        if ((A[1][4]==0 or M14_12==1) and A[2][5]==0):
            if (Left_Col23%2==0 and sum_r23%2!=0 and sum_c23%2!=0 and Top_Row23%2==0):
                if (((A[1][7]==1 or M17_12==0) and A[2][8]==0) and ((A[4][7]==1 or M47_12==0) and A[5][8]==0)) or (((A[1][7]==1 or M17_12==0) and A[2][8]==1) and ((A[4][7]==1 or M47_12==0) and A[5][8]==1)):    
                    if ((Left_Col23-A[1][7])%2!=0 and (sum_r23-A[1][7])%2==0) and((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2!=0):
                        Left_Col23 = Left_Col23-A[1][7]
                        sum_r23 = sum_r23-A[1][7]
                        M17_23=1
                        sum_c23 = sum_c23-A[4][7]
                        Top_Row23=Top_Row23-A[4][7]
                        M47_23=1
                if ((A[1][7]==0 or M17_12==1) and A[2][8]==1) and ((A[4][7]==0 or M47_12==1) and A[5][8]==1):
                    if ((Left_Col23-A[2][8])%2!=0 and (sum_r23-A[2][8])%2==0) and((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2!=0):
                        Left_Col23 = Left_Col23-A[2][8]
                        sum_r23 = sum_r23-A[2][8]
                        M28_23=1
                        sum_c23 = sum_c23-A[5][8]
                        Top_Row23=Top_Row23-A[5][8]
                        M58_23=1
                if ((A[1][7]==1 or M17_12==0) and A[2][8]==0) and ((A[4][7]==0 or M47_12==1) and A[5][8]==1):    
                    if ((Left_Col23-A[1][7])%2!=0 and (sum_r23-A[1][7])%2==0) and((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2!=0):
                        Left_Col23 = Left_Col23-A[1][7]
                        sum_r23 = sum_r23-A[1][7]
                        M17_23=1
                        sum_c23 = sum_c23-A[5][8]
                        Top_Row23=Top_Row23-A[5][8]
                        M58_23=1
                if ((A[1][7]==0 or M17_12==1) and A[2][8]==1) and ((A[4][7]==1 or M47_12==0) and A[5][8]==0):
                    if ((Left_Col23-A[2][8])%2!=0 and (sum_r23-A[2][8])%2==0) and((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2!=0):
                        Left_Col23 = Left_Col23-A[2][8]
                        sum_r23 = sum_r23-A[2][8]
                        M28_23=1
                        sum_c23 = sum_c23-A[4][7]
                        Top_Row23=Top_Row23-A[4][7]
                        M47_23=1
    #Case-6 (OOOO),A[1][4]=0,A[2][5]=0
     # M17_12=0,M47_12=0
        if ((A[1][4]==0 or M14_12==1) and A[2][5]==0):
            if (Left_Col23%2!=0 and sum_r23%2!=0 and sum_c23%2!=0 and Top_Row23%2!=0):
                if (((A[1][7]==1 or M17_12==0) and A[2][8]==0) and ((A[4][7]==1 or M47_12==0) and A[5][8]==0)) or (((A[1][7]==1 or M17_12==0) and A[2][8]==1) and ((A[4][7]==1 or M47_12==0) and A[5][8]==1)):    
                    if ((Left_Col23-A[1][7])%2==0 and (sum_r23-A[1][7])%2==0) and((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2==0):
                        Left_Col23 = Left_Col23-A[1][7]
                        sum_r23 = sum_r23-A[1][7]
                        M17_23=1
                        sum_c23 = sum_c23-A[4][7]
                        Top_Row23=Top_Row23-A[4][7]
                        M47_23=1
                if ((A[1][7]==0 or M17_12==1) and A[2][8]==1) and ((A[4][7]==0 or M47_12==1) and A[5][8]==1):
                    if ((Left_Col23-A[2][8])%2==0 and (sum_r23-A[2][8])%2==0) and((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2==0):
                        Left_Col23 = Left_Col23-A[2][8]
                        sum_r23 = sum_r23-A[2][8]
                        M28_23=1
                        sum_c23 = sum_c23-A[5][8]
                        Top_Row23=Top_Row23-A[5][8]
                        M58_23=1
                if ((A[1][7]==1 or M17_12==0) and A[2][8]==0) and ((A[4][7]==0 or M47_12==1) and A[5][8]==1):
                    if ((Left_Col23-A[1][7])%2==0 and (sum_r23-A[1][7])%2==0) and((sum_c23-A[5][8])%2==0 and (Top_Row23-A[5][8])%2==0):
                        Left_Col23 = Left_Col23-A[1][7]
                        sum_r23 = sum_r23-A[1][7]
                        M17_23=1
                        sum_c23 = sum_c23-A[5][8]
                        Top_Row23=Top_Row23-A[5][8]
                        M58_23=1
                if ((A[1][7]==0 or M17_12==1) and A[2][8]==1) and ((A[4][7]==1 or M47_12==0) and A[5][8]==0):    
                    if ((Left_Col23-A[2][8])%2==0 and (sum_r23-A[2][8])%2==0) and((sum_c23-A[4][7])%2==0 and (Top_Row23-A[4][7])%2==0):
                        Left_Col23 = Left_Col23-A[2][8]
                        sum_r23 = sum_r23-A[2][8]
                        M28_23=1
                        sum_c23 = sum_c23-A[4][7]
                        Top_Row23=Top_Row23-A[4][7]
                        M47_23=1
                        
        
    #Case-7 (OOEE),A[1][7]=0,A[2][8]=0
    if ((A[1][7]==0 or M17_12==1) and A[2][8]==0):
        if (Left_Col23%2!=0 and sum_r23%2!=0 and sum_c23%2==0 and Top_Row23%2==0):
            if (((A[1][4]==1 or M14_12==0) and (A[4][7]==1 or M47_12==0)) and (A[2][5]==0 and A[5][8]==0))or (((A[1][4]==1 or M14_12==0) and (A[4][7]==1 or M47_12==0)) and (A[2][5]==1 and A[5][8]==1)):
                if ((sum_r23-A[1][4])%2==0 and (sum_c23-A[1][4]-A[4][7])%2==0 and (Top_Row23-A[4][7])%2!=0):
                    sum_r23 = sum_r23-A[1][4]
                    sum_c23 = sum_c23-A[1][4]-A[4][7]
                    Top_Row23 = Top_Row23-A[4][7]
                    M14_23=1
                    M47_23=1
            if (((A[1][4]==0 or M14_12==1) and (A[4][7]==0 or M47_12==1)) and (A[2][5]==1 and A[5][8]==1)):
                if ((sum_r23-A[2][5])%2==0 and (sum_c23-A[2][5]-A[5][8])%2==0 and (Top_Row23-A[5][8])%2!=0):
                    sum_r23 = sum_r23-A[2][5]
                    sum_c23 = sum_c23-A[2][5]-A[5][8]
                    Top_Row23 = Top_Row23-A[5][8]
                    M25_23=1
                    M58_23=1
            if (((A[1][4]==1 or M14_12==0) and A[4][7]==0) and (A[2][5]==0 and A[5][8]==1)):
                if ((sum_r23-A[1][4])%2==0 and (sum_c23-A[1][4]-A[5][8])%2==0 and (Top_Row23-A[5][8])%2!=0):
                    sum_r23 = sum_r23-A[1][4]
                    sum_c23 = sum_c23-A[1][4]-A[5][8]
                    Top_Row23 = Top_Row23-A[5][8]
                    M14_23=1
                    M58_23=1
            if ((A[1][4]==0 and (A[4][7]==1 or M47_12==0)) and (A[2][5]==1 and A[5][8]==0)):
                if ((sum_r23-A[2][5])%2==0 and (sum_c23-A[2][5]-A[4][7])%2==0 and (Top_Row23-A[4][7])%2!=0):
                    sum_r23 = sum_r23-A[2][5]
                    sum_c23 = sum_c23-A[2][5]-A[4][7]
                    Top_Row23 = Top_Row23-A[4][7]
                    M25_23=1
                    M47_23=1

    #Case-8 (EEOO),A[4][7]=0,A[5][8]=0
    if (A[4][7]==0 and A[5][8]==0):
        if (Left_Col23%2==0 and sum_r23%2==0 and sum_c23%2!=0 and Top_Row23%2!=0):
            if (((A[1][4]==1 or M14_12==0) and (A[1][7]==1 or M17_12==0)) and (A[2][8]==0 and A[2][5]==0))or (((A[1][4]==1 or M14_12==0) and (A[1][7]==1 or M17_12==0)) and (A[2][8]==0 and A[2][5]==0)):
                if ((Left_Col23-A[1][7])%2and (sum_r23-A[1][7]-A[1][4])%2==0 and (sum_c23-A[1][4])%2==0):
                    sum_r23 = sum_r23-A[1][7]-A[1][4]
                    sum_c23 = sum_c23-A[1][4]
                    Left_Col23 = Left_Col23-A[1][7]
                    M14_23=1
                    M17_23=1
            if (((A[1][4]==0 or M14_12==1) and (A[1][7]==0 or M17_12==1)) and (A[2][8]==1 and A[2][5]==1)):
                if ((Left_Col23-A[2][8])%2and (sum_r23-A[2][8]-A[2][5])%2==0 and (sum_c23-A[2][5])%2==0):
                    sum_r23 = sum_r23-A[2][8]-A[2][5]
                    sum_c23 = sum_c23-A[2][8]
                    Left_Col23 = Left_Col23-A[2][5]
                    M28_23=1
                    M25_23=1
            if (((A[1][4]==1 or M14_12==0) and (A[1][7]==0 or M17_12==1)) and (A[2][8]==1 and A[2][5]==0)):
                if ((Left_Col23-A[2][8])%2and (sum_r23-A[2][8]-A[1][4])%2==0 and (sum_c23-A[1][4])%2==0):
                    sum_r23 = sum_r23-A[2][8]-A[1][4]
                    sum_c23 = sum_c23-A[1][4]
                    Left_Col23 = Left_Col23-A[2][8]
                    M14_23=1
                    M28_23=1
                    
            if (((A[1][4]==0 or M14_12==1) and (A[1][7]==1 or M17_12==0)) and (A[2][8]==0 and A[2][5]==1)):
                if ((Left_Col23-A[1][7])%2and (sum_r23-A[1][7]-A[2][5])%2==0 and (sum_c23-A[2][5])%2==0):
                    sum_r23 = sum_r23-A[1][7]-A[2][5]
                    sum_c23 = sum_c23-A[2][5]
                    Left_Col23 = Left_Col23-A[1][7]
                    M17_23=1
                    M25_23=1



    print "-------------------"
    print Left_Col23,sum_r23,sum_c23,Top_Row23
    print "-------------------"
    if(Left_Col23%2==0 and sum_r23%2==0 and sum_c23%2==0 and Top_Row23%2==0)or(Left_Col23%2!=0 and sum_r23%2==0 and sum_c23%2==0 and Top_Row23%2!=0):
        print("CDC exists, good configuration")
        return 2
    else:
        print("CDC does not exist, bad configuration")
        return 3
        
    #------------ Graph 2 and 3-------End
    
    #------------ Graph 1 and 3-------S
    R1_13 = A[0][6]+A[0][8]        
    R3_13 = A[2][6]+A[2][8]
    C1_13 = A[3][6]+A[3][8]
    C3_13 = A[5][6]+A[5][8]
    Con_fig_M2b2_13 = reshape((A[0][3],A[0][5],A[2][3],A[2][5]),(2,2))
    #print Con_fig_M2b2_13
    E_K3K1_13 = [[R1_13],[R3_13]]
    Con_fig_M3b2_13 = concatenate((E_K3K1_13,Con_fig_M2b2_13), axis = 1)
    #print Con_fig_M3b2_13
    E_K3K2_13 = [[0,C1_13,C3_13]]
    S13 = concatenate((E_K3K2_13,Con_fig_M3b2_13), axis = 0)
    print "Subgraph Color Class 1 & 3"
    print S13
    print " "
    print S13[1:3,0:3]
    sum_r13 = sum(S13[1:3,0:3])
    print 'RowS13um    =  ',sum_r13
    print S13[0:3,1:3]
    sum_c13 = sum(S13[0:3,1:3])
    print 'ColumnS13um =  ',sum_c13
    Top_Row13 = sum(S13[0:1,0:3])
    print "Top Row"
    print S13[0:1,0:3]
    print 'Top_Row13   =  ',Top_Row13
    Left_Col13 = sum(S13[0:3,0:1])
    print "Lef Column"
    print S13[0:3,0:1]
    print 'Left_Col13  =  ',Left_Col13
    print "-------------------"
    print Left_Col13,sum_r13,sum_c13,Top_Row13
    print "-------------------"

    #Case-1 (EEEE) or (OEEO)
    ME_13=0
    if (Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2==0 and Top_Row13%2==0)or(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2==0 and Top_Row13%2!=0):
        ME_13=1
    #Case-2 (OOOO) or (EOOE)   
    if(M03_12==0 and M25_23==0):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[0][3]==1 and A[2][5]==0):
                if ((sum_r13-A[0][3])%2==0 and (sum_c13-A[0][3])%2==0): 
                    sum_r13 = sum_r13-A[0][3]
                    sum_c13 = sum_c13-A[0][3]
            if (A[0][3]==0 and A[2][5]==1):
                if ((sum_r13-A[2][5])%2==0 and (sum_c13-A[2][5])%2==0):
                    sum_r13 = sum_r13-A[2][5]
                    sum_c13=sum_c13-A[2][5]
            if (A[0][3]==1 and A[2][5]==1):
                if ((sum_r13-A[0][3])%2==0 and (sum_c13-A[0][3])%2==0):
                    sum_r13 = sum_r13-A[0][3]
                    sum_c13 = sum_c13-A[0][3]
    if (M03_12==1 and M25_23==0):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[0][3]==1 and A[2][5]==0):
                if (sum_r13%2==0 and sum_c13%2==0):
                    sum_r13 = sum_r13- 0
                    sum_c13 = sum_c13- 0
            if (A[0][3]==0 and A[2][5]==1):
                if ((sum_r13-A[2][5])%2==0 and (sum_c13-A[2][5])%2==0):
                    sum_r13 = sum_r13-A[2][5]
                    sum_c13=sum_c13-A[2][5]
            if (A[0][3]==1 and A[2][5]==1):
                if ((sum_r13-A[2][5])%2==0 and (sum_c13-A[2][5])%2==0):
                    sum_r13 = sum_r13- A[2][5]
                    sum_c13 = sum_c13- A[2][5]
    if (M03_12==0 and M25_23==1):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[0][3]==1 and A[2][5]==0):
                if ((sum_r13-A[0][3])%2==0 and (sum_c13-A[0][3])%2==0):
                    sum_r13 = sum_r13-A[0][3]
                    sum_c13 = sum_c13-A[0][3]
            if (A[0][3]==0 and A[2][5]==1):
                if (sum_r13%2==0 and sum_c13%2==0):
                    sum_r13 = sum_r13- 0
                    sum_c13=sum_c13- 0
            if (A[0][3]==1 and A[2][5]==1):
                if ((sum_r13-A[0][3])%2==0 and (sum_c13-A[0][3])%2==0):
                    sum_r13 = sum_r13-A[0][3]
                    sum_c13 = sum_c13-A[0][3]
    if (M03_12==1 and M25_23==1):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[0][3]==1 and A[2][5]==0):
                if (sum_r13%2==0 and sum_c13%2==0):
                    sum_r13 = sum_r13- 0
                    sum_c13 = sum_c13- 0
            if (A[0][3]==0 and A[2][5]==1):
                if (sum_r13%2==0 and sum_c13%2==0):
                    sum_r13 = sum_r13- 0
                    sum_c13=sum_c13- 0
            if (A[0][3]==1 and A[2][5]==1):
                if (sum_r13%2==0 and sum_c13%2==0):
                    sum_r13 = sum_r13- 0
                    sum_c13 = sum_c13- 0


    #Case-3 (EEOO) or (OEOE)
    if (M36_12==0 and M58_23==0):
        if(Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[3][6]==1 and A[5][8]== 0):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2==0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
            if (A[3][6]==0 and A[5][8]== 1):
                if ((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2==0):
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13 = Top_Row13-A[5][8]
            if (A[3][6]==1 and A[5][8]== 1):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2==0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
            if (A[3][6]==1 and A[5][8]== 0):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
            if (A[3][6]==0 and A[5][8]== 1):
                if ((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2!=0):
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13 = Top_Row13-A[5][8]
            if (A[3][6]==1 and A[5][8]== 1):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
    if (M36_12==1 and M58_23==0):
        if (Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[3][6]==1 and A[5][8]== 0):
                if (sum_c13%2==0 and Top_Row13%2==0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==0 and A[5][8]== 1):
                if ((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2==0):
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13 = Top_Row13-A[5][8]
            if (A[3][6]==1 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2==0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==1 and A[5][8]== 0):
                if (sum_c13%2==0 and Top_Row13%2!=0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==0 and A[5][8]== 1):
                if ((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2!=0):
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13 = Top_Row13-A[5][8]
            if (A[3][6]==1 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2!=0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
    if (M36_12==0 and M58_23==1):
        if (Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[3][6]==1 and A[5][8]== 0):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2==0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
            if (A[3][6]==0 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2==0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==1 and A[5][8]== 1):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2==0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
            if (A[3][6]==1 and A[5][8]== 0):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
            if (A[3][6]==0 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2!=0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==1 and A[5][8]== 1):
                if ((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13 = Top_Row13-A[3][6]
    if (M36_12==1 and M58_23==1):
        if (Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2!=0)or(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (A[3][6]==1 and A[5][8]== 0):
                if (sum_c13%2==0 and Top_Row13%2==0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==0 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2==0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==1 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2==0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==1 and A[5][8]== 0):
                if (sum_c13%2==0 and Top_Row13%2!=0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==0 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2!=0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
            if (A[3][6]==1 and A[5][8]== 1):
                if (sum_c13%2==0 and Top_Row13%2!=0):
                    sum_c13 = sum_c13- 0
                    Top_Row13 = Top_Row13- 0
    #Case-4 (OOEE) or (EOEO) 
    if (M06_12==0 and M28_23==0):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2==0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2!=0):
            if (A[0][6]==1 and A[2][8]==0 ):
                if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]   
            if (A[0][6]==0 and A[2][8]==1 ):
                if ((Left_Col13-A[2][8])%2==0 and (sum_r13-A[2][8])%2==0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
            if (A[0][6]==1 and A[2][8]==1 ):
                if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]
                    
            if (A[0][6]==1 and A[2][8]==0 ):
                if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]   
            if (A[0][6]==0 and A[2][8]==1 ):
                if ((Left_Col13-A[2][8])%2!=0 and (sum_r13-A[2][8])%2==0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
            if (A[0][6]==1 and A[2][8]==1 ):
                if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]
    if (M06_12==1 and M28_23==0):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2==0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2!=0):
            if (A[0][6]==1 and A[2][8]==0 ):
                if (Left_Col13%2==0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0  
            if (A[0][6]==0 and A[2][8]==1 ):
                if ((Left_Col13-A[2][8])%2==0 and (sum_r13-A[2][8])%2==0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
            if (A[0][6]==1 and A[2][8]==1 ):
                if (Left_Col13%2==0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0
            if (A[0][6]==1 and A[2][8]==0 ):
                if (Left_Col13%2!=0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0  
            if (A[0][6]==0 and A[2][8]==1 ):
                if ((Left_Col13-A[2][8])%2!=0 and (sum_r13-A[2][8])%2==0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
            if (A[0][6]==1 and A[2][8]==1 ):
                if (Left_Col13%2!=0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0
    if (M06_12==0 and M28_23==1):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2==0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2!=0):
            if (A[0][6]==1 and A[2][8]==0 ):
                if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]   
            if (A[0][6]==0 and A[2][8]==1 ):
                if (Left_Col13%2==0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0
            if (A[0][6]==1 and A[2][8]==1 ):
                if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]

            if (A[0][6]==1 and A[2][8]==0 ):
                if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]   
            if (A[0][6]==0 and S13[2][0]==1 ):
                if (Left_Col13%2!=0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0
            if (A[0][6]==1 and A[2][8]==1 ):
                if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]
    if (M06_12==1 and M28_23==1):
        if (Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2==0)or(Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2!=0):
            if (A[0][6]==1 and A[2][8]==0 ):
                if (Left_Col13%2==0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0  
            if (A[0][6]==0 and A[2][8]==1 ):
                if (Left_Col13%2==0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0
            if (A[0][6]==1 and A[2][8]==1 ):
                if (Left_Col13%2==0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0

            if (A[0][6]==1 and A[2][8]==0 ):
                if (Left_Col13%2!=0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0  
            if (A[0][6]==0 and A[2][8]==1 ):
                if (Left_Col13%2!=0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0
            if (A[0][6]==1 and A[2][8]==1 ):
                if (Left_Col13%2!=0 and sum_r13%2==0):
                    Left_Col13 = Left_Col13- 0
                    sum_r13 = sum_r13- 0
                    
    #Case-5 (EOOE),A[0][3]=0,A[2][5]=0
    if ((A[0][3]==0 or M03_12==1) and (A[2][5]==0 or M25_23==1 )):
        if (Left_Col13%2==0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2==0):    
            if (((A[0][6]==1 or M06_12==0) and (A[2][8]==0 or M28_23==1)) and ((A[3][6]==1 or M36_12==0) and (A[5][8]==0 or M58_23==1))) or (((A[0][3]==1 or M03_12==0) and (A[2][8]==1 or M28_23==0)) and ((A[3][6]==1 or M36_12==0) and (A[5][8]==1 or M58_23==0))):
                if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][6])%2==0) and((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13=Top_Row13-A[3][6]
            if ((A[0][6]==0 or M06_12==1) and (A[2][8]==1 or M28_23==0)) and ((A[3][6]==0 or M36_12==1) and (A[5][8]==1 or M58_23==0)):    
                if ((Left_Col13-A[2][8])%2!=0 and (sum_r13-A[2][8])%2==0) and((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2!=0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13=Top_Row13-A[5][8]
            if ((A[0][6]==1 or M06_12==0) and (A[2][8]==0 or M28_23==1)) and ((A[3][6]==0 or M36_12==1) and (A[5][8]==1 or M58_23==0)):    
                if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][6])%2==0) and((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2!=0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13=Top_Row13-A[5][8]
            if ((A[0][6]==0 or M06_12==1) and (A[2][8]==1 or M28_23==0)) and ((A[3][6]==1 or M36_12==0) and (A[5][8]==0 or M58_23==1)):    
                if ((Left_Col13-A[2][8])%2!=0 and (sum_r13-A[2][8])%2==0) and((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13=Top_Row13-A[3][6] 
    #Case-6 (OOOO),A[0][3]=0,A[2][5]=0
    if ((A[0][3]==0 or M03_12==1) and (A[2][5]==0 or M25_23==1 )):
        if(Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2!=0 and Top_Row13%2!=0):    
            if (((A[0][6]==1 or M06_12==0) and (A[2][8]==0 or M28_23==1)) and ((A[3][6]==1 or M36_12==0) and (A[5][8]==0 or M58_23==1))) or (((A[0][6]==1 or M06_12==0) and (A[2][8]==1 or M28_23==0)) and ((A[3][6]==1 or M36_12==0) and (A[5][8]==1 or M58_23==0))):
                if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][6])%2==0) and((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13=Top_Row13-A[3][6]
            if ((A[0][6]==0 or M06_12==1) and (A[2][8]==1 or M28_23==0)) and ((A[3][6]==0 or M36_12==1) and (A[5][8]==1 or M58_23==0)):    
                if ((Left_Col13-A[2][8])%2==0 and (sum_r13-A[2][8])%2==0) and((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2==0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13=Top_Row13-A[5][8]
            if ((A[0][6]==1 or M06_12==0) and (A[2][8]==0 or M28_23==1)) and ((A[3][6]==0 or M36_12==1) and (A[5][8]==1 or M58_23==0)):    
                if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][6])%2==0) and((sum_c13-A[5][8])%2==0 and (Top_Row13-A[5][8])%2==0):
                    Left_Col13 = Left_Col13-A[0][6]
                    sum_r13 = sum_r13-A[0][6]
                    sum_c13 = sum_c13-A[5][8]
                    Top_Row13=Top_Row13-A[5][8]
            if ((A[0][6]==0 or M03_12==1) and (A[2][8]==1 or M28_23==0)) and ((A[3][6]==1 or M36_12==0) and (A[5][8]==0 or M58_23==1)):    
                if ((Left_Col13-A[2][8])%2==0 and (sum_r13-A[2][8])%2==0) and((sum_c13-A[3][6])%2==0 and (Top_Row13-A[3][6])%2==0):
                    Left_Col13 = Left_Col13-A[2][8]
                    sum_r13 = sum_r13-A[2][8]
                    sum_c13 = sum_c13-A[3][6]
                    Top_Row13=Top_Row13-A[3][6]

            

    #Case-7 (OOEE),A[0][6]=0,A[2][8]=0
    if ((A[0][6]==0 or M06_12==1) and (A[2][8]==0 or M25_23==1)):
        if(Left_Col13%2!=0 and sum_r13%2!=0 and sum_c13%2==0 and Top_Row13%2==0):    
            if (((A[0][3]==1 or M03_12==0) and (A[3][6]==1 or M36_12==0)) and ((A[2][5]==0 or M25_23==1) and (A[5][8]==0 or M58_23==1))) or (((A[0][3]==1 or M03_12==0) and (A[3][6]==1 or M36_12==0)) and ((A[2][5]==1 or M25_23==0) and (A[5][8]==1 or M58_23==0))):
                if ((sum_r13-A[0][3])%2==0 and (sum_c13-A[0][3]-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    sum_r13 = sum_r13-A[0][3]
                    sum_c13 = sum_c13-A[0][3]-A[3][6]
                    Top_Row13=Top_Row13-A[3][6]
            if (((A[0][3]==0 or M03_12==1) and (A[3][6]==0 or M36_12==1)) and ((A[2][5]==1 or M25_23==0) and (A[5][8]==1 or M58_23==0))): 
                if ((sum_r13-A[2][5])%2==0 and (sum_c13-A[2][5]-A[5][8])%2==0 and (Top_Row13-A[5][8])%2!=0):
                    sum_r13 = sum_r13-A[2][5]
                    sum_c13 = sum_c13-A[2][5]-A[5][8]
                    Top_Row13=Top_Row13-A[5][8]
            if (((A[0][3]==1 or M03_12==0) and (A[3][6]==0 or M36_12==1)) and ((A[2][5]==0 or M25_23==1) and (A[5][8]==1 or M58_23==0))):    
                if ((sum_r13-A[0][3])%2==0 and (sum_c13-A[0][3]-A[5][8])%2==0 and (Top_Row13-A[5][8])%2!=0):
                    sum_r13 = sum_r13-A[0][3]
                    sum_c13 = sum_c13-A[0][3]-A[5][8]
                    Top_Row13=Top_Row13-A[5][8]
            if (((A[0][3]==0 or M03_12==1) and (A[3][6]==1 or M36_12==0)) and ((A[2][5]==1 or M25_23==0) and (A[5][8]==0 or M48_23==1))):    
                if ((sum_r13-A[2][5])%2==0 and (sum_c13-A[2][5]-A[3][6])%2==0 and (Top_Row13-A[3][6])%2!=0):
                    sum_r13 = sum_r13-A[2][5]
                    sum_c13 = sum_c13-A[2][5]-A[3][6]
                    Top_Row13=Top_Row13-A[3][6]
                

    #Case-8 (EEOO),(OEOE),A[3][6]=0,A[5][8]=0
    if ((A[3][6]==0 or M36_12==1) and (A[5][8]==0 or M58_23==1)):
        if(Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2!=0):
            if (((A[0][3]==1 or M03_12==0) and (A[0][6]==1 or M06_12==0)) and ((A[2][5]==0 or M25_23==1) and (A[2][8]==0 or M28_23==1))) or (((A[0][3]==1 or M03_12==0) and (A[0][6]==1 or M06_12==0)) and ((A[2][5]==1 or M25_23==0) and (A[2][8]==1 or M28_23==0))):
                if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][3]-A[0][6])%2==0 and (sum_c13-A[0][3])%2==0):
                   Left_Col13 = Left_Col13-A[0][6]
                   sum_r13 = sum_r13-A[0][3]-A[0][6]
                   sum_c13 = sum_c13-A[0][3]
            if (((A[0][3]==0 or M03_12==1) and (A[0][6]==0 or M06_12==1)) and ((A[2][5]==1 or M25_23==0) and (A[2][8]==1 or M28_23==0))):    
               if ((Left_Col13-A[2][8])%2!=0 and (sum_r13-A[2][5]-A[2][8])%2==0 and (sum_c13-A[2][5])%2==0):
                   Left_Col13 = Left_Col13-A[2][8]
                   sum_r13 = sum_r13-A[2][5]-A[2][8]
                   sum_c13 = sum_c13-A[2][5]
            if (((A[0][3]==1 or M03_12==0) and (A[0][6]==0 or M06_12==1)) and ((A[2][5]==0 or M25_23==1) and (A[2][8]==1 or M28_23==0))):    
               if ((Left_Col13-A[2][8])%2!=0 and (sum_r13-A[2][8]-A[0][3])%2==0 and (sum_c13-A[0][3])%2==0):
                   Left_Col13 = Left_Col13-A[2][8]
                   sum_r13 = sum_r13-A[2][8]-A[0][3]
                   sum_c13 = sum_c13-A[0][3]
            if (((A[0][3]==0 or M03_12==1) and (A[0][6]==1 or M06_12==0)) and ((A[2][5]==1 or M25_23==0) and (A[2][8]==0 or M28_23==1))):    
               if ((Left_Col13-A[0][6])%2!=0 and (sum_r13-A[0][6]-A[2][5])%2==0 and (sum_c13-A[2][5])%2==0):
                   Left_Col13 = Left_Col13-A[0][6]
                   sum_r13 = sum_r13-A[0][6]-A[2][5]
                   sum_c13 = sum_c13-A[2][5]

        if(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2!=0 and Top_Row13%2==0):
            if (((A[0][3]==1 or M03_12==0) and (A[0][6]==1 or M06_12==0)) and ((A[2][5]==0 or M25_23==1) and (A[2][8]==0 or M28_23==1))) or (((A[0][3]==1 or M03_12==0) and (A[0][6]==1 or M06_12==0)) and ((A[2][5]==1 or M25_23==0) and (A[2][8]==1 or M28_23==0))):
                if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][3]-A[0][6])%2==0 and (sum_c13-A[0][3])%2==0):
                   Left_Col13 = Left_Col13-A[0][6]
                   sum_r13 = sum_r13-A[0][3]-A[0][6]
                   sum_c13 = sum_c13-A[0][3]
            if (((A[0][3]==0 or M03_12==1) and (A[0][6]==0 or M06_12==1)) and ((A[2][5]==1 or M25_23==0) and (A[2][8]==1 or M28_23==0))):    
               if ((Left_Col13-A[2][8])%2==0 and (sum_r13-A[2][5]-A[2][8])%2==0 and (sum_c13-A[2][5])%2==0):
                   Left_Col13 = Left_Col13-A[2][8]
                   sum_r13 = sum_r13-A[2][5]-A[2][8]
                   sum_c13 = sum_c13-A[2][5]
            if (((A[0][3]==1 or M03_12==0) and (A[0][6]==0 or M06_12==1)) and ((A[2][5]==0 or M25_23==1) and (A[2][8]==1 or M28_23==0))):    
               if ((Left_Col13-A[2][8])%2==0 and (sum_r13-A[2][8]-A[0][3])%2==0 and (sum_c13-A[0][3])%2==0):
                   Left_Col13 = Left_Col13-A[2][8]
                   sum_r13 = sum_r13-A[2][8]-A[0][3]
                   sum_c13 = sum_c13-A[0][3]
            if (((A[0][3]==0 or M03_12==1) and (A[0][6]==1 or M06_12==0)) and ((A[2][5]==1 or M25_23==0) and (A[2][8]==0 or M28_23==1))):    
               if ((Left_Col13-A[0][6])%2==0 and (sum_r13-A[0][6]-A[2][5])%2==0 and (sum_c13-A[2][5])%2==0):
                   Left_Col13 = Left_Col13-A[0][6]
                   sum_r13 = sum_r13-A[0][6]-A[2][5]
                   sum_c13 = sum_c13-A[2][5]
    
            

    print "-------------------"
    print Left_Col13,sum_r13,sum_c13,Top_Row13
    print "-------------------"
    if(Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2==0 and Top_Row13%2==0)or(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2==0 and Top_Row13%2!=0):
       print("CDC exists, good configuration")
    else:
        print("CDC does not exist, bad configuration")
    #------------ Graph 1 and 3-------End

    # Decesion making
    if (Left_Col12%2==0 and sum_r12%2==0 and sum_c12%2==0 and Top_Row12%2==0) or (Left_Col12%2!=0 and sum_r12%2==0 and sum_c12%2==0 and Top_Row12%2!=0):
        if(Left_Col23%2==0 and sum_r23%2==0 and sum_c23%2==0 and Top_Row23%2==0)or(Left_Col23%2!=0 and sum_r23%2==0 and sum_c23%2==0 and Top_Row23%2!=0):
            if(Left_Col13%2==0 and sum_r13%2==0 and sum_c13%2==0 and Top_Row13%2==0)or(Left_Col13%2!=0 and sum_r13%2==0 and sum_c13%2==0 and Top_Row13%2!=0):
                print("CDC exists, good configuration")
                return 2
            else:
                print("CDC does not exist, bad configuration")
                return 3

#--------------------------------
# The Operations() fuction is used to generate matrices and pass on
# to the the function Config_Check() for decision mking about
# Good or Bad configuration, where Good means that 3 disjoint graphs
# form and good frame(Cycle Double Cover-CDC exists) and Bad represents
# that CDC does not exists.


def Operations(x):
    # Arrays initialization and reshaping to 9 by 9 matrix
    x_A = [[0]*9]*9
    x_A1 = [[0]*9]*9
    x_A2 = [[0]*9]*9
    x_A3 = [[0]*9]*9
    x_A4 = [[0]*9]*9
    x_A5 = [[0]*9]*9
    x_A6 = [[0]*9]*9
    x_A7 = [[0]*9]*9
    x_A12 = [[0]*9]*9
    x_A15 = [[0]*9]*9
    x_A18 = [[0]*9]*9

    # New variables
    x_A19 = [[0]*9]*9
    x_A19 = reshape(x,(9,9))
    x_A20 = [[0]*9]*9
    x_A20 = reshape(x,(9,9))
    x_A21 = [[0]*9]*9
    x_A21 = reshape(x,(9,9))
    x_A22 = [[0]*9]*9
    x_A22 = reshape(x,(9,9))
    x_A23 = [[0]*9]*9
    x_A23 = reshape(x,(9,9))
    x_A24 = [[0]*9]*9
    x_A24 = reshape(x,(9,9))
    x_A25 = [[0]*9]*9
    x_A25 = reshape(x,(9,9))
    x_A26 = [[0]*9]*9
    x_A26 = reshape(x,(9,9))
    x_A27 = [[0]*9]*9
    x_A27 = reshape(x,(9,9))
    x_A28 = [[0]*9]*9
    x_A28 = reshape(x,(9,9))
    x_A29 = [[0]*9]*9
    x_A29 = reshape(x,(9,9))
    x_A30 = [[0]*9]*9
    x_A30 = reshape(x,(9,9))
    x_A31 = [[0]*9]*9
    x_A31 = reshape(x,(9,9))
    x_A32 = [[0]*9]*9
    x_A32 = reshape(x,(9,9))
    x_A33 = [[0]*9]*9
    x_A33 = reshape(x,(9,9))
    x_A34 = [[0]*9]*9
    x_A34 = reshape(x,(9,9))
    x_A35 = [[0]*9]*9
    x_A35 = reshape(x,(9,9))
    x_A36 = [[0]*9]*9
    x_A36 = reshape(x,(9,9))
    x_A37 = [[0]*9]*9
    x_A37 = reshape(x,(9,9))
    x_A,x_A1,x_A2,x_A3,x_A4,x_A5,x_A6,x_A7,x_A12,x_A15,x_A18 = reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9)),reshape(x,(9,9))
    i = 0
    while (i < 32):
        #Case:1 Origional
        i = i + 1
        Config_Check(x_A)
        if Case1 == 2:
            break
        #Case:2 C1,S(C2,C3)
        print ("Fixing C1, Swapping C2 & C3")
        x_A = None
        x1 = reshape(x_A1,(9,9))
        x1_1 = col_swap(x1,4,5)
        x1_2 = row_swap(x1_1,4,5)
        #print x1_2
        i = i + 1
        Config_Check(x1_2)
        if Case2 == 2:
            break
        #Case:3 C2,S(C1,C3)
        print ("Fixing C2,Swapping C1 & C3")
        x1,x1_1,x1_2,x_A1 = None, None,None,None
        x2 = reshape(x_A2,(9,9))
        x2_1 = col_swap(x2,3,5)
        x2_2 = row_swap(x2_1,3,5)
        #print x2_2
        i = i + 1
        Config_Check(x2_2)
        if Case3 == 2:
            break
        #Case:4 C3,S(C1,C2)
        print ("Fixing C3,Swapping C1 & C2")
        x2,x2_1,x2_2,x_A2 = None, None,None,None
        x3 = reshape(x_A3,(9,9))
        x3_1 = col_swap(x3,3,4)
        x3_2 = row_swap(x3_1,3,4)
        #print x3_2
        i = i + 1
        Config_Check(x3_2)
        if Case4 == 2:
            break
        #Case:5 R1,S(R2,R3)
        print ("Fixing R1,Swapping R2 & R3")
        x3,x3_1,x3_2,x_A3 = None, None,None,None
        x4 = reshape(x_A4,(9,9))
        x4_1 = row_swap(x4,1,2)
        x4_2 = col_swap(x4_1,1,2)
        #print x4_2
        i = i + 1
        Case5 = Config_Check(x4_2)
        if Case5 == 2:
            break
        #Case:6 R2,S(R1,R3)
        print ("Fixing R2,Swapping R1 & R3")
        x4,x4_1,x4_2,x_A4= None, None,None,None
        x5 = reshape(x_A5,(9,9))
        x5_1 = row_swap(x5,0,2)
        x5_2 = col_swap(x5_1,0,2)
        #print x5_2
        i = i + 1
        Case6 = Config_Check(x5_2)
        if Case6 == 2:
            break
        #Case:7 R3,S(R1,R2)
        print ("Fixing R3,Swapping R1 & R2")
        x5,x5_1,x5_2,x_A5= None, None,None,None
        x6 = reshape(x_A6,(9,9))
        x6_1 = row_swap(x6,0,1)
        x6_2 = col_swap(x6_1,0,1)
        #print x6_2
        i = i + 1
        Case7 = Config_Check(x6_2)
        if Case7 == 2:
            break
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        print ("Changing in Cyclic Order_Column 3->4,4->5,5->3")
        x6,x6_1,x6_2,x_A6= None, None,None,None
        x7 = reshape(x_A7,(9,9))
        x8_1 = col_swap(x7,3,4)
        x8_2 = row_swap(x8_1,3,4)
        x9_1 = col_swap(x8_2,4,5)
        x9_2 = row_swap(x9_1,4,5)
        #print x9_2
        i = i + 1
        Case8 = Config_Check(x9_2)
        if Case8 == 2:
            break
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        print ("Changing in Anti-Cyclic Order_Column 3->5,5->4,4->3")
        x7,x8_1,x8_2,x9_1,x9_2= None, None,None,None,None
        x10 = reshape(x_A12,(9,9))
        x11_1 = col_swap(x10,3,5)
        x11_2 = row_swap(x11_1,3,5)
        x12_1 = col_swap(x11_2,4,5)
        x12_2 = row_swap(x12_1,4,5)
        #print x12_2
        i = i + 1
        Case9 = Config_Check(x12_2)
        if Case9 == 2:
            break
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        print ("Changing in Cyclic Order_Row 0->1,1->2,2->0")
        x10,x11_1,x11_2,x12_2,x_A12= None, None,None,None,None
        x13 = reshape(x_A15,(9,9))
        x14_1 = row_swap(x13,0,1)
        x14_2 = col_swap(x14_1,0,1)
        x15_1 = row_swap(x14_2,1,2)
        x15_2 = col_swap(x15_1,1,2)
        #print x15_2
        i = i + 1
        Case10 = Config_Check(x15_2)
        if Case10 == 2:
            break
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        print ("Changing in Anti-Cyclic Order_Row 0->2,2->1,1->0")
        x13,x14_1,x14_2,x15_1,x15_2,x_A15= None, None,None,None,None,None
        x16 = reshape(x_A18,(9,9))
        x17_1 = row_swap(x16,0,2)
        x17_2 = col_swap(x17_1,0,2)
        x18_1 = row_swap(x17_2,1,2)
        x18_2 = col_swap(x18_1,1,2)
        #print x18_2
        i = i + 1
        Case11 = Config_Check(x18_2)
        if Case11 == 2:
            break
        x16,x17_1,x17_2,x18_1,x18_2,x_A18= None, None,None,None,None,None
        #--------------------------------------------------
        #Case:12, Fixing C1 and Swapping(C2,C3) + CyclicRow
        #Case:2 C1,S(C2,C3)
        print ("Fixing C1 and Swapping(C2,C3) + CyclicRow")
        C1_23S_CR_x = reshape(x_A19,(9,9))
        C1_23S_CR_x_1 = col_swap(C1_23S_CR_x,4,5)
        C1_23S_CR_x_2 = row_swap(C1_23S_CR_x_1,4,5)
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        C1_23S_CR_x_01 = reshape(C1_23S_CR_x_2,(9,9))
        C1_23S_CR_x_02 = row_swap(C1_23S_CR_x_01,0,1)
        C1_23S_CR_x_03 = col_swap(C1_23S_CR_x_02,0,1)
        C1_23S_CR_x_04 = row_swap(C1_23S_CR_x_03,1,2)
        C1_23S_CR_x_0 = col_swap(C1_23S_CR_x_04,1,2)
        #print x15_2
        i = i + 1
        Case12 = Config_Check(C1_23S_CR_x_0)
        if Case12 == 2:
            break
        #--------------------------------------------------
        #Case:13, Fixing C2 and Swapping(C1,C3) + CyclicRow
        #Case:3 C2,S(C1,C3)
        print ("Fixing C2 and Swapping(C1,C3) + CyclicRow")
        C2_13S_CR_x = reshape(x_A20,(9,9))
        C2_13S_CR_x_1 = col_swap(C2_13S_CR_x,3,5)
        C2_13S_CR_x_2 = row_swap(C2_13S_CR_x_1,3,5)
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        C2_13S_CR_x_01 = reshape(C2_13S_CR_x_2,(9,9))
        C2_13S_CR_x_02 = row_swap(C2_13S_CR_x_01,0,1)
        C2_13S_CR_x_03 = col_swap(C2_13S_CR_x_02,0,1)
        C2_13S_CR_x_04 = row_swap(C2_13S_CR_x_03,1,2)
        C2_13S_CR_x_0 = col_swap(C2_13S_CR_x_04,1,2)
        i = i + 1
        Case13 = Config_Check(C2_13S_CR_x_0)
        if Case13 == 2:
            break
        #--------------------------------------------------
        
        #Case:14, Fixing C3 and Swapping(C1,C2) + CyclicRow
        #Case:4 C3,S(C1,C2)
        print ("Fixing C3 and Swapping(C1,C2) + CyclicRow")
        C3_12S_CR_x = reshape(x_A21,(9,9))
        C3_12S_CR_x_1 = col_swap(C3_12S_CR_x,3,4)
        C3_12S_CR_x_2 = row_swap(C3_12S_CR_x_1,3,4)
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        C3_12S_CR_x_01 = reshape(C3_12S_CR_x_1,(9,9))
        C3_12S_CR_x_02 = row_swap(C3_12S_CR_x_01,0,1)
        C3_12S_CR_x_03 = col_swap(C3_12S_CR_x_02,0,1)
        C3_12S_CR_x_04 = row_swap(C3_12S_CR_x_03,1,2)
        C3_12S_CR_x_0 = col_swap(C3_12S_CR_x_04,1,2)
        i = i + 1
        Case14 = Config_Check(C3_12S_CR_x_0)
        if Case14 == 2:
            break
        #--------------------------------------------------
        #Case:15, Fixing C1 and Swapping(C2,C3) + Anti-CyclicRow
        #Case:3 C2,S(C1,C3)
        print ("Fixing C1 and Swapping(C2,C3) + Anti-CyclicRow")
        C1_23S_ACR_x = reshape(x_A22,(9,9))
        C1_23S_ACR_x_1 = col_swap(C1_23S_ACR_x,3,5)
        C1_23S_ACR_x_2 = row_swap(C1_23S_ACR_x_1,3,5)
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        C1_23S_ACR_x_01 = reshape(C1_23S_ACR_x_2,(9,9))
        C1_23S_ACR_x_02 = row_swap(C1_23S_ACR_x_01,0,2)
        C1_23S_ACR_x_03 = col_swap(C1_23S_ACR_x_02,0,2)
        C1_23S_ACR_x_04 = row_swap(C1_23S_ACR_x_03,2,1)
        C1_23S_ACR_x_0 = col_swap(C1_23S_ACR_x_04,2,1)
        i = i + 1
        Case15 = Config_Check(C1_23S_ACR_x_0)
        if Case15 == 2:
            break
        #--------------------------------------------------
        #Case:16, Fixing C2 and Swapping(C1,C3) + Anti-CyclicRow
        #Case:3 C2,S(C1,C3)
        print ("Fixing C2 and Swapping(C1,C3) + Anti-CyclicRow")
        C2_13S_ACR_x = reshape(x_A23,(9,9))
        C2_13S_ACR_x_1 = col_swap(C2_13S_ACR_x,3,5)
        C2_13S_ACR_x_2 = row_swap(C2_13S_ACR_x_1,3,5)
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        C2_13S_ACR_x_01 = reshape(C2_13S_ACR_x_2,(9,9))
        C2_13S_ACR_x_02 = row_swap(C2_13S_ACR_x_01,0,2)
        C2_13S_ACR_x_03 = col_swap(C2_13S_ACR_x_02,0,2)
        C2_13S_ACR_x_04 = row_swap(C2_13S_ACR_x_03,2,1)
        C2_13S_ACR_x_0 = col_swap(C2_13S_ACR_x_04,2,1)
        i = i + 1
        Case16 = Config_Check(C2_13S_ACR_x_0)
        if Case16 == 2:
            break
        #--------------------------------------------------
        #Case:17, Fixing C3 and Swapping(C1,C2) + Anti-CyclicRow
        #Case:4 C3,S(C1,C2)
        print ("Fixing C3 and Swapping(C1,C2) + Anti-CyclicRow")
        C3_12S_ACR_x = reshape(x_A24,(9,9))
        C3_12S_ACR_x_1 = col_swap(C3_12S_ACR_x,3,4)
        C3_12S_ACR_x_2 = row_swap(C3_12S_ACR_x_1,3,4)
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        C3_12S_ACR_x_01 = reshape(C3_12S_ACR_x_2,(9,9))
        C3_12S_ACR_x_02 = row_swap(C3_12S_ACR_x_01,0,2)
        C3_12S_ACR_x_03 = col_swap(C3_12S_ACR_x_02,0,2)
        C3_12S_ACR_x_04 = row_swap(C3_12S_ACR_x_03,2,1)
        C3_12S_ACR_x_0 = col_swap(C3_12S_ACR_x_04,2,1)
        i = i + 1
        Case17 = Config_Check(C3_12S_ACR_x_0)
        if Case17 == 2:
            break
        #--------------------------------------------------
        #Case:18, Fixing R1 and Swapping(R2,R3) + CyclicColumn
        #Case:5 R1,S(R2,R3)
        print ("Fixing R1 and Swapping(R2,R3) + CyclicColumn")
        R1_23S_CC_x = reshape(x_A24,(9,9))
        R1_23S_CC_x_1 = row_swap(R1_23S_CC_x,1,2)
        R1_23S_CC_x_2 = col_swap(R1_23S_CC_x_1,1,2)
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        R1_23S_CC_x_01 = reshape(R1_23S_CC_x_2,(9,9))
        R1_23S_CC_x_02 = col_swap(R1_23S_CC_x_01,3,4)
        R1_23S_CC_x_03 = row_swap(R1_23S_CC_x_02,3,4)
        R1_23S_CC_x_04 = col_swap(R1_23S_CC_x_03,4,5)
        R1_23S_CC_x_0 = row_swap(R1_23S_CC_x_04,4,5)
        i = i + 1
        Case18 = Config_Check(R1_23S_CC_x_0)
        if Case18 == 2:
            break
        #--------------------------------------------------
        #Case:19, Fixing R2 and Swapping(R1,R3) + CyclicColumn
        #Case:6 R2,S(R1,R3)
        print ("Fixing R2 and Swapping(R1,R3) + CyclicColumn")
        R2_13S_CC_x = reshape(x_A26,(9,9))
        R2_13S_CC_x_1 = row_swap(R2_13S_CC_x,0,2)
        R2_13S_CC_x_2 = col_swap(R2_13S_CC_x_1,0,2)
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        R2_13S_CC_x_01 = reshape(R2_13S_CC_x_2,(9,9))
        R2_13S_CC_x_02 = col_swap(R2_13S_CC_x_01,3,4)
        R2_13S_CC_x_03 = row_swap(R2_13S_CC_x_02,3,4)
        R2_13S_CC_x_04 = col_swap(R2_13S_CC_x_03,4,5)
        R2_13S_CC_x_0 = row_swap(R2_13S_CC_x_04,4,5)
        i = i + 1
        Case19 = Config_Check(R2_13S_CC_x_0)
        if Case19 == 2:
            break
        #--------------------------------------------------
        #Case:20, Fixing R3 and Swapping(R1,R2) + CyclicColumn
        #Case:7 R3,S(R1,R2)
        print ("Fixing R3 and Swapping(R1,R2) + CyclicColumn")
        R3_12S_CC_x = reshape(x_A27,(9,9))
        R3_12S_CC_x_1 = row_swap(R3_12S_CC_x,0,1)
        R3_12S_CC_x_2 = col_swap(R3_12S_CC_x_1,0,1)
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        R3_12S_CC_x_01 = reshape(R3_12S_CC_x_2,(9,9))
        R3_12S_CC_x_02 = col_swap(R3_12S_CC_x_01,3,4)
        R3_12S_CC_x_03 = row_swap(R3_12S_CC_x_02,3,4)
        R3_12S_CC_x_04 = col_swap(R3_12S_CC_x_03,4,5)
        R3_12S_CC_x_0 = row_swap(R3_12S_CC_x_04,4,5)
        i = i + 1
        Case20 = Config_Check(R3_12S_CC_x_0)
        if Case20 == 2:
            break
        #--------------------------------------------------
        #Case:21, Fixing R1 and Swapping(R2,R3) + Anti-CyclicColumn
        #Case:5 R1,S(R2,R3)
        print ("Fixing R1 and Swapping(R2,R3) + Anti-CyclicColumn")
        R1_23S_ACC_x = reshape(x_A27,(9,9))
        R1_23S_ACC_x_1 = row_swap(R1_23S_ACC_x,1,2)
        R1_23S_ACC_x_2 = col_swap(R1_23S_ACC_x_1,1,2)
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        R1_23S_ACC_x_01 = reshape(R1_23S_ACC_x_2,(9,9))
        R1_23S_ACC_x_02 = col_swap(R1_23S_ACC_x_01,3,5)
        R1_23S_ACC_x_03 = row_swap(R1_23S_ACC_x_02,3,5)
        R1_23S_ACC_x_04 = col_swap(R1_23S_ACC_x_03,4,5)
        R1_23S_ACC_x_0 = row_swap(R1_23S_ACC_x_04,4,5)
        i = i + 1
        Case21 = Config_Check(R1_23S_ACC_x_0)
        if Case21 == 2:
            break
        #--------------------------------------------------
        #Case:22, Fixing R2 and Swapping(R1,R3) + Anti-CyclicColumn
        #Case:6 R2,S(R1,R3)
        print ("Fixing R2 and Swapping(R1,R3) + Anti-CyclicColumn")
        R2_13S_ACC_x = reshape(x_A28,(9,9))
        R2_13S_ACC_x_1 = row_swap(R2_13S_ACC_x,0,2)
        R2_13S_ACC_x_2 = col_swap(R2_13S_ACC_x_1,0,2)
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        R2_13S_ACC_x_01 = reshape(R2_13S_ACC_x_2,(9,9))
        R2_13S_ACC_x_02 = col_swap(R2_13S_ACC_x_01,3,5)
        R2_13S_ACC_x_03 = row_swap(R2_13S_ACC_x_02,3,5)
        R2_13S_ACC_x_04 = col_swap(R2_13S_ACC_x_03,4,5)
        R2_13S_ACC_x_0 = row_swap(R2_13S_ACC_x_04,4,5)
        i = i + 1
        Case22 = Config_Check(R2_13S_ACC_x_0)
        if Case22 == 2:
            break
        #--------------------------------------------------
        #Case:23, Fixing R3 and Swapping(R1,R2) + Anti-CyclicColumn
        print ("Fixing R3 and Swapping(R1,R2) + Anti-CyclicColumn")
        R3_12S_ACC_x = reshape(x_A29,(9,9))
        R3_12S_ACC_x_1 = row_swap(R3_12S_ACC_x,0,1)
        R3_12S_ACC_x_2 = col_swap(R3_12S_ACC_x_1,0,1)
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        R3_12S_ACC_x_01 = reshape(R3_12S_ACC_x_2,(9,9))
        R3_12S_ACC_x_02 = col_swap(R3_12S_ACC_x_01,3,5)
        R3_12S_ACC_x_03 = row_swap(R3_12S_ACC_x_02,3,5)
        R3_12S_ACC_x_04 = col_swap(R3_12S_ACC_x_03,4,5)
        R3_12S_ACC_x_0 = row_swap(R3_12S_ACC_x_04,4,5)
        i = i + 1
        Case23 = Config_Check(R3_12S_ACC_x_0)
        if Case23 == 2:
            break
        #--------------------------------------------------
        #Case:24,CyclicColumn,CyclicRow
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        print ("CyclicColumn,3->4,4->5,5->3,CyclicRow 0->1,1->2,2->0")
        CC_CR_x = reshape(x_A30,(9,9))
        CC_CR_x_1 = col_swap(CC_CR_x,3,4)
        CC_CR_x_2 = row_swap(CC_CR_x_1,3,4)
        CC_CR_x_3 = col_swap(CC_CR_x_2,4,5)
        CC_CR_x_4 = row_swap(CC_CR_x_3,4,5)
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        CC_CR_x_01 = reshape(CC_CR_x_4,(9,9))
        CC_CR_x_02 = row_swap(CC_CR_x_01,0,1)
        CC_CR_x_03 = col_swap(CC_CR_x_02,0,1)
        CC_CR_x_04 = row_swap(CC_CR_x_03,1,2)
        CC_CR_x_0 = col_swap(CC_CR_x_04,1,2)
        i = i + 1
        Case24 = Config_Check(CC_CR_x_0)
        if Case24 == 2:
            break
        #--------------------------------------------------
        #Case:25,CyclicColumn,Anti-CyclicRow
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        print ("CyclicColumn,3->4,4->5,5->3,Anti-CyclicRow,0->2,2->1,1->0")
        CC_ACR_x = reshape(x_A31,(9,9))
        CC_ACR_x_1 = col_swap(CC_ACR_x,3,4)
        CC_ACR_x_2 = row_swap(CC_ACR_x_1,3,4)
        CC_ACR_x_3 = col_swap(CC_ACR_x_2,4,5)
        CC_ACR_x_4 = row_swap(CC_ACR_x_3,4,5)
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        CC_ACR_x_01 = reshape(CC_ACR_x_4,(9,9))
        CC_ACR_x_02 = row_swap(CC_ACR_x_01,0,2)
        CC_ACR_x_03 = col_swap(CC_ACR_x_02,0,2)
        CC_ACR_x_04 = row_swap(CC_ACR_x_03,2,1)
        CC_ACR_x_0 = col_swap(CC_ACR_x_04,2,1)
        i = i + 1
        Case25 = Config_Check(CC_ACR_x_0)
        if Case25 == 2:
            break
        #--------------------------------------------------
        #Case:26,Anti-CyclicColumn,CyclicRow
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        print ("Anti-CyclicColumn,3->5,5->4,4->3,CyclicRow,0->1,1->2,2->0")
        AC_CR_x = reshape(x_A32,(9,9))
        AC_CR_x_1 = col_swap(AC_CR_x,3,5)
        AC_CR_x_2 = row_swap(AC_CR_x_1,3,5)
        AC_CR_x_3 = col_swap(AC_CR_x_2,4,5)
        AC_CR_x_4 = row_swap(AC_CR_x_3,4,5)
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        AC_CR_x_01 = reshape(AC_CR_x_4,(9,9))
        AC_CR_x_02 = row_swap(AC_CR_x_01,0,1)
        AC_CR_x_03 = col_swap(AC_CR_x_02,0,1)
        AC_CR_x_04 = row_swap(AC_CR_x_03,1,2)
        AC_CR_x_0 = col_swap(AC_CR_x_04,1,2)
        i = i + 1
        Case26 = Config_Check(AC_CR_x_0)
        if Case26 == 2:
            break
        #--------------------------------------------------
        #Case:27,Anti-CyclicColumn,Anti-CyclicRow
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        print ("Anti-CyclicColumn,3->5,5->4,4->3,Anti-CyclicRow,0->2,2->1,1->0")
        AC_ACR_x = reshape(x_A33,(9,9))
        AC_ACR_x_1 = col_swap(AC_ACR_x,3,5)
        AC_ACR_x_2 = row_swap(AC_ACR_x_1,3,5)
        AC_ACR_x_3 = col_swap(AC_ACR_x_2,4,5)
        AC_ACR_x_4 = row_swap(AC_ACR_x_3,4,5)
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        AC_ACR_x_01 = reshape(AC_ACR_x_4,(9,9))
        AC_ACR_x_02 = row_swap(AC_ACR_x_01,0,2)
        AC_ACR_x_03 = col_swap(AC_ACR_x_02,0,2)
        AC_ACR_x_04 = row_swap(AC_ACR_x_03,2,1)
        AC_ACR_x_0 = col_swap(AC_ACR_x_04,2,1)
        i = i + 1
        Case27 = Config_Check(AC_ACR_x_0)
        if Case27 == 2:
            break
        #--------------------------------------------------
        #Case:28,CyclicRow,CyclicColumn  
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        print ("CyclicRow,0->1,1->2,2->0,CyclicColumn,3->4,4->5,5->3")
        CR_CC_x = reshape(x_A34,(9,9))
        CR_CC_x_1 = row_swap(CR_CC_x,0,1)
        CR_CC_x_2 = col_swap(CR_CC_x_1,0,1)
        CR_CC_x_3 = row_swap(CR_CC_x_2,1,2)
        CR_CC_x_4 = col_swap(CR_CC_x_3,1,2)
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        CR_CC_x_01 = reshape(x_A7,(9,9))
        CR_CC_x_02 = col_swap(CR_CC_x_01,3,4)
        CR_CC_x_03 = row_swap(CR_CC_x_02,3,4)
        CR_CC_x_04 = col_swap(CR_CC_x_03,4,5)
        CR_CC_x_0 = row_swap(CR_CC_x_04,4,5)
        i = i + 1
        Case28 = Config_Check(CR_CC_x_0)
        if Case28 == 2:
            break
        #--------------------------------------------------
        #Case:29,CyclicRow,Anti-CyclicColumn
        #Case:10 Cyclic Row order 0->1,1->2,2->0
        print ("CyclicRow,0->1,1->2,2->0,Anti-CyclicColumn,3->5,5->4,4->3 ")
        CR_ACC_x = reshape(x_A35,(9,9))
        CR_ACC_x_1 = row_swap(CR_ACC_x,0,1)
        CR_ACC_x_2 = col_swap(CR_ACC_x_1,0,1)
        CR_ACC_x_3 = row_swap(CR_ACC_x_2,1,2)
        CR_ACC_x_4 = col_swap(CR_ACC_x_3,1,2)
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        CR_ACC_x_01 = reshape(CR_ACC_x_4,(9,9))
        CR_ACC_x_02 = col_swap(CR_ACC_x_01,3,5)
        CR_ACC_x_03 = row_swap(CR_ACC_x_02,3,5)
        CR_ACC_x_04 = col_swap(CR_ACC_x_03,4,5)
        CR_ACC_x_0 = row_swap(CR_ACC_x_04,4,5)
        i = i + 1
        Case29 = Config_Check(CR_ACC_x_0)
        if Case29 == 2:
            break
        #--------------------------------------------------
        #Case:30,Anti-CyclicRow,CyclicColumn
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        print ("Anti-CyclicRow,0->2,2->1,1->0,CyclicColumn,3->4,4->5,5->3")
        ACR_CC_x = reshape(x_A36,(9,9))
        ACR_CC_x_1 = row_swap(ACR_CC_x,0,2)
        ACR_CC_x_2 = col_swap(ACR_CC_x_1,0,2)
        ACR_CC_x_3 = row_swap(ACR_CC_x_2,2,1)
        ACR_CC_x_4 = col_swap(ACR_CC_x_3,2,1)
        #Case:8 Cyclic Colmn order 3->4,4->5,5->3
        ACR_CC_x_01 = reshape(ACR_CC_x_4,(9,9))
        ACR_CC_x_02 = col_swap(ACR_CC_x_01,3,4)
        ACR_CC_x_03 = row_swap(ACR_CC_x_02,3,4)
        ACR_CC_x_04 = col_swap(ACR_CC_x_03,4,5)
        ACR_CC_x_0 = row_swap(ACR_CC_x_04,4,5)
        i = i + 1
        Case30 = Config_Check(ACR_CC_x_0)
        if Case30 == 2:
            break
        #--------------------------------------------------
        #Case:31,Anti-CyclicRow,Anti-CyclicColumn
        #Case:11 Anti-Cyclic Order_Row 0->2,2->1,1->0
        print ("Anti-CyclicRow,0->2,2->1,1->0,Anti-CyclicColumn,3->5,5->4,4->3")
        ACR_ACC_x = reshape(x_A37,(9,9))
        ACR_ACC_x_1 = row_swap(ACR_ACC_x,0,2)
        ACR_ACC_x_2 = col_swap(ACR_ACC_x_1,0,2)
        ACR_ACC_x_3 = row_swap(ACR_ACC_x_2,1,2)
        ACR_ACC_x_4 = col_swap(ACR_ACC_x_3,1,2)
        #Case:9 Anti-Cyclic Colmn order 3->5,5->4,4->3
        ACR_ACC_x_01 = col_swap(ACR_ACC_x_4,3,5)
        ACR_ACC_x_02 = row_swap(ACR_ACC_x_01,3,5)
        ACR_ACC_x_03 = col_swap(ACR_ACC_x_02,4,5)
        ACR_ACC_x_0 = row_swap(ACR_ACC_x_03,4,5)
        i = i + 1
        Case31 = Config_Check(ACR_ACC_x_0)
        if Case31 == 2:
            break
        #Case:32, Symmtric Matrix
        i = i + 1






#--------------------------------
from networkx import *
from numpy import *
'''A = [[0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0]]'''

A = [[0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0]]

operations(A)
#if (i==63):
