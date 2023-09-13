-- Keep a log of any SQL queries you execute as you solve the mystery.

--querys crime scene reports for specified date and street
SELECT * FROM crime_scene_reports WHERE year = 2021 AND day = 28 AND month = 7 AND street = 'Humphrey Street';
--id 295 is our report, more specfic version of above query
SELECT * FROM crime_scene_reports WHERE id=295;

--report says 3 interviews conducted, each report mentions the bakery, took place at 10:15am
SELECT * FROM interviews WHERE year = 2021 AND day = 28 AND month = 7 and transcript like ('%bakery%');

--info from 3 reports: 1) sometime within 10 min after the theft, the thief got into a car, look for cars leaving within this time frame 2) thief was at atm on leggett street in the morning 3)thief is taking flight out of fityville tomorrow, he called someone for less than a minute for them to purchase the flight tickets

--atm information, thiefs account number found here
SELECT * FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

--license plate information found here, all cars leaving within 10 minutes of the theft
SELECT * FROM bakery_security_logs WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute BETWEEN 15 AND 25 AND activity = 'exit';

--gives us options for our thief caller and reciever number; calls that took place for less than a min on this day

--the phone number of our accomplice, lets get his name
SELECT receiver FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration < 60 AND caller = '(367) 555-5533';

--earliest flight out of fiftyville on July 29
SELECT * FROM flights JOIN airports ON flights.origin_airport_id = airports.id WHERE year = 2021 AND day = 29 AND month = 7 AND flights.id = 36;

--As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call,
--I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief
--then asked the person on the other end of the phone to purchase the flight ticket.

--all passengers on this early flight out of fiftyville, gives us options for our thiefs passport number
SELECT * FROM passengers JOIN flights ON flights.id = passengers.flight_id WHERE flights.id = 36 AND passport_number = 5773159633;
SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE flights.id = 36 AND passport_number = 5773159633;

SELECT * FROM airports WHERE id = 4;


--have a passport number and license plate to work with now
-- this query gives us information for people who have a license plate seen within 10 min of the crime and have a bank account number used at the atm

--All people who left the bakery and used the atm and have a flight booked out the next morning and made a call within 10 min of the theft
SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'))
AND passport_number IN (SELECT passport_number FROM passengers JOIN flights ON flights.id = passengers.flight_id WHERE flights.id = 36)
AND phone_number IN (SELECT caller FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration < 60)
AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute BETWEEN 15 AND 25 AND activity = 'exit');



--the phone number of our accomplice/the receiver, lets get his name
SELECT * FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration < 60 AND caller = '(367) 555-5533');


