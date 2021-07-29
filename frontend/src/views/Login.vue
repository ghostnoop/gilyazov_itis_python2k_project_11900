<template>
  <section class="login__section">
    <header class="login__header">
      <div class="logo__login">
        <h2 class="logo__header__text">Iremember</h2>
      </div>
    </header>
    <div class="login__content">
      <app-login-form></app-login-form>
    </div>
    <div class="login__background">
    </div>
  </section>
</template>

<script>
import AppLoginForm from "@/components/Login/AppLoginForm";

export default {
  name: "Login",
  components: {AppLoginForm}
}
</script>

<style>

</style>
