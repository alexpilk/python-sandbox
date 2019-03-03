name = 'Oleksii'
company = 'Nokia'
job = 'software developer'
hobbies = ['playing prog metal', 'irritating people']

bio = """
My name is {name}. I am a {job} at {company}.
In my spare time I like {hobbies} etc.
""".format(
    name=name,
    company=company,
    job=job,
    hobbies=', '.join(hobbies)
)

print(bio)
