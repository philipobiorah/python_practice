guestlist = ['chigozie', 'tii', 'samba', 'uncle inno', 'semper' ]


for i in range(len(guestlist)-1):
    print(f"{guestlist[i].title()} you are invited to my Graduation Ceremoney")


cannot_make_it = ['semper','samba']



for p in cannot_make_it:
    guestlist.remove(p)


guestlist.insert(1, "Atimor")

print("Current List:")
for guest in guestlist:
    print(guest.title())
