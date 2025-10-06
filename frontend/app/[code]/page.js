'use client'

import { useEffect } from 'react'

export default function RedirectPage({ params }) {
  useEffect(() => {
    const redirect = async () => {
      try {
        const res = await fetch(`http://10.149.108.162:30080/${params.code}`)
        if (!res.ok) throw new Error('Invalid short URL')

        const data = await res.json()
        if (data.original_url) {
          window.location.href = data.original_url
        }
      } catch (err) {
        console.error(err)
      }
    }

    redirect()
  }, [params.code])

  return <p>Redirecting...</p>
}
