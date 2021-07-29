<template>
  <app-sprite></app-sprite>
  <section class="main__section board__section">
    <app-header-main></app-header-main>
    <app-content-board></app-content-board>

    <app-popup-member></app-popup-member>
    <app-popup-invitation></app-popup-invitation>
  </section>

  <app-member-menu></app-member-menu>
  <app-create-board></app-create-board>
</template>

<script>
import AppSprite from "@/sprite/AppSprite";
import AppHeaderMain from "@/components/Main/AppHeaderMain";
import AppMemberMenu from "@/components/Main/AppMemberMenu";
import AppCreateBoard from "@/components/Main/AppCreateBoard";
import AppContentBoard from "@/components/Board/AppContentBoard";
import AppPopupMember from "@/components/Board/AppPopupMember";
import AppPopupInvitation from "@/components/Board/AppPopupInvitation";

export default {
  name: "Board",
  components: {
    AppSprite,
    AppHeaderMain,
    AppMemberMenu,
    AppCreateBoard,
    AppContentBoard,
    AppPopupMember,
    AppPopupInvitation
  }
}
</script>

<style scoped>

</style>