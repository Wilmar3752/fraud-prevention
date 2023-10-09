from gradio_client import Client

client = Client("https://wilmars-fraud-meli-app.hf.space/")
result = client.predict(
				4,	# int | float  in 'a' Number component
				0.5,	# int | float  in 'b' Number component
				1000,	# int | float  in 'c' Number component
				1,	# int | float  in 'd' Number component
				0.28,	# int | float  in 'e' Number component
				12,	# int | float  in 'f' Number component
				"BR",	# str  in 'g' Textbox component
				36,	# int | float  in 'h' Number component
				"cat_4744ece",	# str  in 'j' Textbox component
				0.6366103624,	# int | float  in 'k' Number component
				2470,	# int | float  in 'l' Number component
				308,	# int | float  in 'm' Number component
				1,	# int | float  in 'n' Number component
				"Y",	# str  in 'o' Textbox component
				"Y",	# str  in 'p' Textbox component
				"2020-03-18 09:31:52",	# str  in 'fecha' Textbox component
				24.89,	# int | float  in 'monto' Number component
				93,	# int | float  in 'score' Number component
				api_name="/predict"
)
print(result)