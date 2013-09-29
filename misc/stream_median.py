import random
def create_file():
    with open("workfile_float","w") as f:
        array = [random.normalvariate(100,15) for _ in range(1000000)]
        for item in array:
            f.write(str(item)+"\n")


def stream_median(filename):
    median_est = 0
    with open(filename,"r") as f:
        for line in f:
            if float(line.rstrip()) > median_est:
                median_est += 1
            elif float(line.rstrip()) < median_est:
                median_est -= 1
    print median_est

create_file()
stream_median("workfile_float")
