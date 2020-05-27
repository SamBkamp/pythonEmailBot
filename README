# A python email bot

I wrote this little python app when I was told to send a emails to 88 different students. The emails were all fundamentally the same, they were supposed to welcome the students to a service, and deliver their username and password. The format was similar to

```
Hi [Student Name],

Welcome to the service, we look forward to working with you.

Here are your login details:

Email: [Students email]
Password: [Students password]

Many Thanks,
github.com/SamBkamp
```

Of course, I am not about to write 88 emails like this without at lest trying to automate it. So here I am.

I used the [yagmail](https://github.com/kootenpv/yagmail) library to do most of the heavy lifting. I basically jut did the formatting. Which, thanks to pythons str.replace() method was super easy.


## Tips if you want to try use this

- Follow the yagmail guide
- gmail will automatically block login from your app (for security reasons apparently) so I enabled 2fa and used the app-password feature. This worked fine.
- Store your password in the keyring, makes life easier.