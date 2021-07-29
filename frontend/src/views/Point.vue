<template>
  <app-sprite></app-sprite>
  <section class="main__section">
    <app-header-main></app-header-main>
    <h1 class="center">Точки</h1>
    <app-point-card></app-point-card>

    <app-footer-main></app-footer-main>
  </section>

</template>

<script>
import AppSprite from "@/sprite/AppSprite";
import AppHeaderMain from "@/components/Main/AppHeaderMain";
import AppMemberMenu from "@/components/Main/AppMemberMenu";
import AppContentMain from "@/components/Main/AppContentMain";
import AppCreateTeam from "@/components/Main/AppCreateTeam";
import AppCreateBoard from "@/components/Main/AppCreateBoard";
import AppFooterMain from "@/components/Main/AppFooterMain";
import AppPointCard from "@/components/Point/AppPointCard"

export default {
  name: "Point",
  components: {
    AppPointCard,
    AppSprite, AppHeaderMain, AppMemberMenu, AppContentMain, AppCreateTeam,AppCreateBoard,AppFooterMain}
}
</script>

<style scoped>

</style>
