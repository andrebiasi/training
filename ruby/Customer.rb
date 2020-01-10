class Customer
	@@no_of_customers = 0

	def initialize(id, name)
		@cust_id = id
		@cust_name = name
	end

	def display_details()
		puts("#@cust_id  #@cust_name")
	end

	def total_no_customers()
		@@no_of_customers += 1
		puts("Total number of customers: #@@no_of_customers")
	end
end

cust1 = Customer.new("1", "Andre")
cust1.display_details()
cust1.total_no_customers()

cust2 = Customer.new("2", "Olga")
cust1.total_no_customers()