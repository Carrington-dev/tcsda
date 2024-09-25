## Endpoints

# Foreign Exchange API

This includes authentication with the following endpoints

## Auth Endpoints </>
```bash
#  Under nginx docker-compose
/api/v1/auth/users/ # all users
/api/v1/auth/users/me/ # all users
/api/v1/auth/users/me/ # all users
/api/v1/auth/jwt/create/
/api/v1/auth/jwt/refresh/
/api/v1/auth/users/resend_activation/
/api/v1/auth/users/reset_password/
/api/v1/auth/users/set_password/
/api/v1/auth/users/set_email/
/api/v1/auth/users/activation/
```

## Forex API 

```bash
#  Under nginx docker-compose
/api/v1/transactions/orders/
/api/v1/transactions/orders/<UUID> # PUT
/api/v1/transactions/orders/<UUID> # PUT
```
## API-KEY Authentication

Managed to add API-KEY authentication via X-Api-Key on headers. Also managed to add user authentication with token based authentication with djoser and simple-jwt on one simple container

```bash
# 
# Example of API-KEYs <FIXs0Rft.UwfTi7EMNy0tA3caoIq9jh1a6JIuwbut>
# Once created it should be stored otherwise you won't be able to see it again
```


## Project Structure

```python
/foreweb # forex APIs
/payflex # authentication APIs
/nginx # merges two api into one domain
docker-compose.yaml
```

## Project Exploration

To explore using different domains/sub-domains for each service
```bash
offering.tcsda.org.za
auth.tcsda.org.za
# Just an idea
```
