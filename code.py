#Google Map database and construction of Minimum Cost Spanning Tree From any selected City
#Name: Shruti Jain
#Roll-No.: A-24

#CODE:

INF = 9999999

N = 7 # number of cities in graph

#creating graph by adjacency matrix method
G = [[0, 1219, 448,813,710,864,1103], #nagpur
     [1219,0,1340,982,839,1540,349],  #banglore
     [448,1340,0,587,609,389,1557],   #Indore
     [813, 982, 587, 0, 163, 533, 1276],#mumbai
     [710, 839, 609, 163, 0, 706, 1200],#pune
     [864, 1540, 389, 533, 706, 0, 1826],#ahemdabad
     [1103, 349, 1557, 1276, 1200, 1826, 0]]#chennai

selected_city = [0, 0, 0, 0, 0, 0, 0]

no_edge = 0

cities = ['Nagpur', 'Banglore', 'Indore', 'Mumbai', 'Pune', 'Ahemdabad', 'Chennai']

selected_city[0] = True



# printing cities and distance distance between them


print("\n\nCities     :     Distance\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_city[m]:
            for n in range(N):
                if ((not selected_city[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(cities[a] + " to " + cities[b] + ":" + str(G[a][b]))
    selected_city[b] = True
    no_edge += 1