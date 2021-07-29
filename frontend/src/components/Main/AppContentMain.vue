<template>
  <section class="main__content">
    <app-main-content-right></app-main-content-right>
    <app-main-content-left></app-main-content-left>
  </section>
</template>

<script>
import AppMainContentLeft from "@/components/Main/AppMainContentLeft";
import AppMainContentRight from "@/components/Main/AppMainContentRight";

export default {
  name: "AppContentMain",
  components: {AppMainContentRight, AppMainContentLeft}
}
</script>

<style scoped>

</style>