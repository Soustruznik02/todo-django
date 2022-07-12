# TODO:
  1. Vytvorit django projekt s nazvem TODO
  2. Vytvorit nize specifikovane django modely s relacemi
  3. Vytvorit Vami specifikovane omezeni a validace pro vlastnosti modelu (max_len, 
  max_digits, cascade on delete, atd.)
  4. Vytvorit Administracni views pro nize specifikovane modely

# Modely:
  - Task
    - id
    - created_at
    - update_at
    - owner (User model - one to many)
    - is_completed
    - title
  - User
    - id
    - created_at
    - updated_at
    - is_active
    - email
    - password

# Pozadavky pro odevzdani zadani:
  - odevzdat projekt jako .zip ci jiny format archivu.
  - v projektu musi byt uvedeny requirements.txt pro zreprodukovani integrace
    projektu.
  - nadale tez v projektu musi byt migracni soubory

# Tech stack:
  - Python 3.10
  - Django 4.0
  - Sqlite 3
