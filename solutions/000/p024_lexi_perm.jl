# Euler Project
# Problem 24: https://projecteuler.net/problem=24

# Compute lexicographs of a string and find the millionth lexicograph of digits 0,1,2,3,4,5,6,7,8,9.
#  To run in Julia, run the following: <julia_install_dir> p024_lexi_perm.jl
function swap(x, a, b)
    i = x[a]
    x[a] = x[b]
    x[b] = i
end

function perm(arr, x, st, en)
    if st == en
        y = copy(x)
        push!(arr, y)
    else
        perm(arr, x, st + 1, en)
        for i = (st + 1):en
            a = copy(x[st])
            x[st] = x[i]
            x[i] = a
            perm(arr, x, st + 1, en)
            x[i] = x[st]
            x[st] = a
        end
    end
end

# Generates array in x_perms from array x
x_perms = []

#x = [0,1,2]
x = [0,1,2,3,4,5,6,7,8,9]

# perm(x_perms, x1, 1, 3)

perm(x_perms, x, 1, 10)

print(sort(x_perms)[1000000])