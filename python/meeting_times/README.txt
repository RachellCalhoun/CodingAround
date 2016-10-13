This program takes in any number of sets of number ranges, which should include a start and end time.
It will merge or condense these number ranges giving an outcome of how many number sets (or ranges) that are necessary.

Originally written for meeting times, it could be used for other number sets.

Input and output examples:

meeting times with two gaps :
input: condense_meeting_times([(20, 22), (21, 22), (25, 30), (33, 35)])
output: [(20, 22), (25, 30), (33, 35)]

meeting times with one gap:
input: condense_meeting_times([(20, 22), (21, 22), (25, 30), (18, 24)])
output [(18, 24), (25, 30)]

meeting times with no gap:
input: condense_meeting_times([(20, 22), (21, 22), (18, 24)])
output: [(18, 24)]

example given with instructions:
input: condense_meeting_times([(20, 22), (21, 22), (25, 30)])
output: [(20, 22), (25, 30)]


This program was written in response to the problem presented below:


"At EventBoard we handle a lot of calendar data and we often want to find the available times for a group of people.

For this exercise a meeting is stored as a tuple of integers (start_time, end_time) where the integers represent the number of 30 minute blocks past 12am.

For example

(20, 22)  # a meeting from 10 am -- 11 am
(21, 22)  # a meeting from 10:30 am -- 11 am
Write a function called condense_meeting_times() that takes a list of meeting time ranges and returns a list of condensed ranges. For example,given [(20, 22), (21, 22), (25, 30)] it will output [(20,22), (25,30)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Bonuses:

For bonus points, write the same function but assume the (start_time, end_time) are Unix timestamps.
For even more bonus points, write the same function but assume the (start_time, end_time) are ISO-8601 datetime strings."
