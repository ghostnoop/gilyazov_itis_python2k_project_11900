<template>
  <header class="header_home">
    <div class="header__home--inner">
      <div class="home__logo">
        <svg class="symbol__trello">
          <use xlink:href="#trello"></use>
        </svg>
        <span class="logo__name">Iremember</span>
      </div>
      <nav class="home_nav">
        <router-link to="/login" class="notext-decoration">
          <a href="#" class="home__login--link">Войти</a>
        </router-link>
        <router-link to="/registration" class="notext-decoration">
          <a href="#" class="home__registration--link">Регистрация</a>
        </router-link>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeaderHome"
}
</script>

<style scoped>

</style>
