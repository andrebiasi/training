x = 3

case
when x == 1
	puts 'it is 1'
when x < 3
	puts 'greater than 1'
when (3..5).include?(x)
	puts 'between 3 and 5'
else
	puts 'other'
end

case x
when 1
	puts 'it is 1'
when 2
	puts 'it is 2'
else
	puts 'it is not 1 or 2'
end