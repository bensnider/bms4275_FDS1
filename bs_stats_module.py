### Computation Options Creation
## Mean
def mean(data) :
    mean = sum(data)/len(data)
    return mean
## Variance
def var(data) :
    mean = sum(data)/len(data)
    dif = [n - mean for n in data]
    sq_dif = [n**2 for n in dif]
    sum_sq = sum(sq_dif)
    var = sum_sq / (len(data)-1)
    return var
## Standard Deviation
def sd(data) :
    mean = sum(data)/len(data)
    dif = [n - mean for n in data]
    sq_dif = [n**2 for n in dif]
    sum_sq = sum(sq_dif)
    sd_sqr = sum_sq / (len(data)-1)
    sd = sd_sqr**0.5
    return sd
## Standard Error
def se(data) :
    mean = sum(data)/len(data)
    dif = [n - mean for n in data]
    sq_dif = [n**2 for n in dif]
    sum_sq = sum(sq_dif)
    sd_sqr = sum_sq / (len(data)-1)
    sd = sd_sqr**0.5
    ss_sqr = (len(data))**0.5
    se = sd / ss_sqr
    return se
## Z-Score for a new observation
def z_score(x, y) :
    mean = sum(x)/len(x)
    dif = [n - mean for n in x]
    sq_dif = [n**2 for n in dif]
    sum_sq = sum(sq_dif)
    sd_sqr = sum_sq / (len(x)-1)
    sd = sd_sqr**0.5
    z = (y - mean) / sd
    return z
## Summary of the statistics
def summ(data) :
    mean = sum(data)/len(data)
    dif = [n - mean for n in data]
    sq_dif = [n**2 for n in dif]
    sum_sq = sum(sq_dif)
    var = sum_sq / (len(data)-1)
    sd_sqr = sum_sq / (len(data)-1)
    sd = sd_sqr**0.5
    ss_sqr = (len(data))**0.5
    se = sd / ss_sqr
    return f"Sample Size: {len(data)} \nMean: {mean} \nStandard Deviation: {sd} \nStandard Error: {se} \n"
