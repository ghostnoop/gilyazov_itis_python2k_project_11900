<template>
  <section class="home_page">
    <div class="notfound__content">
      <div class="notfound__info">
        <div class="notfound__title">404</div>
        <div class="notfound__subtitle">Такой страницы не найдено</div>
      </div>
      <router-link to="/login" v-slot="{navigate}" class="notext-decoration">
        <a href="#" class="home__lets--go">Войти</a>
      </router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: "NotFound"
}
</script>

<style scoped>

</style>