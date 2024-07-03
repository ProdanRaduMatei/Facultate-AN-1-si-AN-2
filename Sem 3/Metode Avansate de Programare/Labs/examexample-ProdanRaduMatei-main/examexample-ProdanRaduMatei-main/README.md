# APM - Practical Examination Repository
A bus company requires an automatic system for booking. All available routes are contained in a relational
database table. A route has a source city, a destination city, the departure and arrival times, the total
available number of seats and the price for one ticket.
1. Show all routes in a list (1p), sorted by departure city and departure time. Use Java streams for
   this sorting (1p). If you do not use Java streams, the maximum score is 0.5p.
2. The client has a window allowing them to choose the source city from a combo box. The
   destination city combo box will be automatically updated to contain only the cities reachable from
   the selected source city (2p).
3. After the client chooses the source and destination cities, a new list will show all available routes,
   for the selected cities, with the following information: source city, destination city, departure and
   arrival times, duration and ticket price (1.5p).
4. A client can select the desired route and book a given number of tickets. The available number of
   seats for that route must be updated (1p). The total price will be shown in the client’s window
   (2p). If there are not sufficient tickets available, the application will show a message in a new
   window (0.5p).
   Bonus:
   Show 2 client windows, which both update as the clients make bookings. Use the Observer design pattern.
   (1p)
