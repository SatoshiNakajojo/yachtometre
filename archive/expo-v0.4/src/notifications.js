/* Yachtomètre — notification du matin.

   Limite connue : une notification locale ne peut pas connaître le cours
   du BTC au moment où elle se déclenche. On programme donc, à chaque
   ouverture de l'app, le bulletin du lendemain à partir du dernier
   mouvement observé. Pour un vrai bulletin quotidien il faudra un push
   serveur — c'est le chantier de la phase 8. */

import * as Notifications from 'expo-notifications';
import { Platform } from 'react-native';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true, shouldPlaySound: false, shouldSetBadge: false,
  }),
});

export async function demanderPermission() {
  if (Platform.OS === 'android') {
    await Notifications.setNotificationChannelAsync('bulletin', {
      name: 'Bulletin du matin',
      importance: Notifications.AndroidImportance.DEFAULT,
    });
  }
  const { status } = await Notifications.requestPermissionsAsync();
  return status === 'granted';
}

export async function programmerBulletin(texte) {
  await Notifications.cancelAllScheduledNotificationsAsync();
  await Notifications.scheduleNotificationAsync({
    content: { title: 'Le Yachtomètre', body: texte },
    trigger: { hour: 8, minute: 0, repeats: true, channelId: 'bulletin' },
  });
}

export async function toutAnnuler() {
  await Notifications.cancelAllScheduledNotificationsAsync();
}
