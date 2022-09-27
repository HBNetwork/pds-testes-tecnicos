

def move_sonda(sonda, moves):
    x = sonda[0]
    y = sonda[1]
    d = sonda[2]

    for m in moves:
        if m == 'L':
            if d == 'N':
                d = 'W'
            elif d == 'W':
                d = 'S'
            elif d == 'S':
                d = 'E'
            elif d == 'E':
                d = 'N'
        elif m == 'R':
            if d == 'N':
                d = 'E'
            elif d == 'E':
                d = 'S'
            elif d == 'S':
                d = 'W'
            elif d == 'W':
                d = 'N'
        elif m == 'M':
            if d == 'E':
                x += 1
            elif d == 'N':
                y +=1
            elif d == 'S':
                y -= 1
            elif d == 'W':
                x -= 1

    return f'{x} {y} {d}'

def main():
  assert move_sonda([1, 2, 'N'], "LMLMLMLMM") == "1 3 N"
  assert move_sonda([3, 3, 'E'], "MMRMMRMRRM") == "5 1 E"

if __name__ == "__main__":
  main()
  print("Success!")
