#!/usr/bin/env ruby

class MegaGreeter
    attr_accessor :names

    def initialize(names = "World")
        @names = names
    end

    def say_hi
        if @names.nil?
            puts "..."
        elsif @names.respond_to?("join")
            puts "Goodbye #{@names.join(",")}, come back soon!"
        else
            puts "Goodbye #{@names}. Come back soon!"
        end
    end
 end

if __FILE__ == $0
    mg = MegaGreeter.new
    mg.say_hi
#    mg.say_bye

    mg.names = "Zeke"
    mg.say_hi
#    mg.say_bye

    mg.names = ["Albert", "Brenda", "Charles"]
    mg.say_hi
#    mg.say_bye

    mg.names = nil
    mg.say_hi
#    mg.say_bye
 end
