from collections import Dict as D

fn part1() raises:

    var file = open("input.txt", "r").read()
    var first = List[Int]()
    var second = List[Int]()

    var lines = file.splitlines()

    for line in lines:
        var nums = line[].split(" ")
        
        var filtered_nums = List[String]()
        for n in nums:
            if n[] != "":
                filtered_nums.append(n[])

        first.append(int(filtered_nums[0]))
        second.append(int(filtered_nums[1]))

    sort[stable=False](first)
    sort[stable=False](second)

    var total = 0
    for i in range(len(first)):
        total += abs(first[i] - second[i])
    
    print(total)

fn part2() raises:

    var lines = open("input.txt", "r").read().splitlines()

    var first = List[Int]()
    var counts = D[Int, Int]()

    for line in lines:
        var uf_nums = line[].split(" ")

        var nums = List[Int]()

        for ufn in uf_nums:
            if ufn[] != "":
                nums.append(int(ufn[]))

        first.append(int(nums[0]))

        counts[int(nums[1])] = counts.get(int(nums[1]), 0) + 1

    var total = 0

    for n in first:
        total += (counts.get(n[], 0) * n[])

    print(total)




fn main() raises:
    part1()
    part2()
