<template>
  <div class="home__content">
    <div class="home__info">
      <h2 class="home__info--title">
        <b>Iremember</b> помогает людям <br> сохранять память <br> о родствениках.
      </h2>
      <p class="home__info--subtext">

      </p>
      <div>
        <router-link to="/login" v-slot="{navigate}" class="notext-decoration">
          <a href="#" class="home__lets--go">Давай начнем!</a>
        </router-link>
      </div>
    </div>
    <div class="home__picture">
      <img src="img/family.png" width="1000" height="1000" class="home__img" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: "AppBodyHome"
}
</script>

<style scoped>

</style>
