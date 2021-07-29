<template>
  <form class="login__form" method="post">
    <div id="error" class="error__block" v-if="error.status">
      <p class="error__message">
        {{ error.message }}
      </p>
    </div>
    <h1 class="login__form--title">Вход в Trello</h1>
    <div class="form__group">
      <input type="email" name="email" class="login__form--field" v-model="user.email"
             placeholder="Укажите адрес электронной почты">
    </div>
    <div class="form__group">
      <input type="text" name="username" class="login__form--field" v-model="user.full_name" placeholder="Введите имя">
    </div>
    <div class="form__group">
      <input type="password" name="password" class="login__form--field" v-model="user.password"
             placeholder="Введите пароль">
    </div>
    <div class="form__group">
      <input type="password" name="rep_password" class="login__form--field" v-model="rep_password"
             placeholder="Повторите пароль">
    </div>
    <button type="button" class="login__btn--input" v-on:click="btnRegistration">Зарегистрироваться</button>
  </form>
</template>

<script>
import router from "@/router";

export default {
  name: "AppRegistration",
  data: () => ({
    user: {
      'email': '',
      'full_name': '',
      'password': '',
    },
    errors: {
      error_rep: 'Пароли не совпадают',
      error_email: 'Аккаунт с таким адресом электронной почты существует',
      error_empty: 'Заполните все поля',
      error: 'Ошибка:('
    },
    rep_password: '',
    error: {
      status: false,
      message: ''
    },
  }),
  methods: {
    btnRegistration() {
      if (this.user.password !== '' && this.user.email !== '' && this.user.full_name !== '') {
        this.error.status = false
        this.error.message = ''

        fetch('http://127.0.0.1:8000/register/client', {
          method: 'post',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.user),
          mode: "cors"
        })
            .then(response => response)
            .then(result => {
              console.log(result)
              console.log(this.user)

              let result_json = result.json()


              if (result.status === 201) {
                router.push('/login')
              } else if (result.status === 400) {
                this.error.status = true
                this.error.message = result.errors[0]
              } else {
                this.error.status = true
                this.error.message = this.errors.error
              }
            })
      } else if (this.rep_password !== this.user.password) {
        this.error.status = true
        this.error.message = this.errors.error_rep
      } else {
        this.error.status = true
        this.error.message = this.errors.error_empty
      }

    }
  }
}
</script>

<style scoped>

</style>
