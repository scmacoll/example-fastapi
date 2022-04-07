### Alembic - Database migration tool

--

**allows incremental changes to databases**

>**Steps**
>**1. connect alembic to database** via ~/alembic/env.py & ~/alembic.ini
>__
>2. `$` **alembic revision** - creates a py file under /alembic/versions that contains all of our changes with alembic
>+ this file contains two functions -
>`def upgrade():` - changes a table
>`def downgrade():` - removes table
>__
>3. **setup code for these two functions** ie. in **upgrade**; add new columns for the pre-existing model Class. in **downgrade**; delete created table
>__
>4. **run upgrade function in terminal** -
>`$` alembic upgrade #
// 'create posts table'
>__
>5. **run `$` _revision_ again**, (like a git branch).
Update a model table with a new column. When updating, logic needs to be written in **both** functions.

____
>check alembic current revision: 
`$` _alembic current_
>check alembic latest revision:
`$` _alembic heads_
upgrade latest revision:
`$` _alembic upgrade head_
`||`
`$` _alembic upgrade #_

___
>6. **downgrade alembic to earlier version:**
`$` _alembic downgrade <down_revision>_
`||`
`$` _alembic downgrade -1_
____
>\\\\ every update add a new _alembic revision_ \\\\

>upgrade to revision level:
`$` _alembic upgrade + #_
____
>7. **Implement relationship between Users & Posts -**
*Create new alembic revision
$ -m "add foreign key to posts table
>Add foreign key column to source table & join with referent table with both functions.
*upgrade to alembic head
>__
>8. **Add last 2 columns to posts table**
`$` _alembic upgrade +1_
>__
>9. **Create Votes Table**
> via auto-generate command:
> `$` _alembic revision --autogenerate -m "text"_
> then:
> `$` _alembic upgrade head_
> 
>\\\\alembic can detect the table model from sqlalchemy - _import models & assign it to the metadata_\\\\

### </>
____

### CORS Policy
**C**ross **O**rigin **R**esource **S**haring
  >Allows requests from a web browser on one domain to a sever on a different domain.
  >__
  _eg. enabling CORS in our API with google.com allows google to send a fetch request to our API server_

_By default, configuring an API will only access to a a web browser running on the same domain on our server to make requests._

To allow exterior domains to talk to you API, insert CORS middleware from CORS documentation.

`middle ware` = function that runs before every request

| request :> main.py :> middleware :> routers | 

**`["*"]` == public access to API**
___

### Setting Up Git

`$` pip freeze
in _(venv)_ shows all the dependencies & packages needed for our git repository project.
>**1. Put all dependencies in requirements.txt file**
>`$`_pip freeze > requirements.txt_
__
\\\\ installing requirements.txt for a git user = `$ pip install -r requirements.txt`\\\\
