<template>
  <app-sprite></app-sprite>
  <section class="main__section">
    <app-header-main></app-header-main>
    <h1 class="center">Заказы</h1>
    <app-footer-main></app-footer-main>
  </section>
  <app-member-menu></app-member-menu>
  <app-create-team></app-create-team>
  <app-create-board></app-create-board>
</template>

<script>
import AppSprite from "@/sprite/AppSprite";
import AppHeaderMain from "@/components/Main/AppHeaderMain";
import AppMemberMenu from "@/components/Main/AppMemberMenu";
import AppContentMain from "@/components/Main/AppContentMain";
import AppCreateTeam from "@/components/Main/AppCreateTeam";
import AppCreateBoard from "@/components/Main/AppCreateBoard";
import AppFooterMain from "@/components/Main/AppFooterMain";

export default {
  name: "Order",
  components: {AppSprite, AppHeaderMain, AppMemberMenu, AppContentMain, AppCreateTeam,AppCreateBoard,AppFooterMain}
}
</script>

<style scoped>

</style>
