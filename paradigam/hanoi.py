def hanoi(disks, source, helper, destination):
  #base condition
  if(disks == 1):
    print('Disk {} moves from tower {} to tower {}. '.format(disks, source, destination))
    return
  
  #recusive calls in which function calls yourself
  hanoi(disks -1, source, destination, helper)
  print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
  hanoi(disks - 1, helper, source, destination)

#drive code
disks = int(input('Number of disks to be replaced: '))
hanoi(disks, 'A', 'B', 'C')