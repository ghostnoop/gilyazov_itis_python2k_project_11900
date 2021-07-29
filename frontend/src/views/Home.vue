<template>
  <section class="home_page">
    <app-header-home></app-header-home>
    <app-body-home></app-body-home>
  </section>
</template>

<script>
import AppSprite from "@/sprite/AppSprite";
import AppHeaderHome from "@/components/Home/AppHeaderHome";
import AppBodyHome from "@/components/Home/AppBodyHome";

export default {
  name: "Home",
  components: {AppHeaderHome, AppBodyHome}
}
</script>

<style scoped>

</style>
